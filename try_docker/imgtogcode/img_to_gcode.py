import os
import sys
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from rdp import rdp
from tkinter import Tk
from skimage.morphology import medial_axis, thin
from skimage.morphology import skeletonize
from tkinter.filedialog import askopenfilename


def show_im_by_plot(im, name='Image'): # показать изображение
    plt.figure(name)
    plt.imshow(im,cmap='gray')
    plt.show()


def choose_img_ui(): # выбрать файл используя gui
    Tk().withdraw()
    filename = askopenfilename(initialdir= os.getcwd(),
                                title="Please select a file:")
    print(filename)
    return filename


def import_img(path): # считать изображения по пути
    im = cv.imread(path)
    return im   


def thresh_im(im): # получить чёрно-белое изображение (простой порог)
    imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(imgray, (3, 3), 0)
    ret, thresh = cv.threshold(blurred, 200, 255, 0) #200, 255, 0
    return thresh


def medline(thresh): # получить центральную линию фигуры (1 пиксель)
    iminvert = cv.bitwise_not(thresh)
    iminvert[iminvert == 255] = 1
    med_axis = skeletonize(iminvert)
    med_axis = med_axis + 0
    med_axis[med_axis == 0] = 255
    med_axis[med_axis == 1] = 0
    return med_axis


def find_endpoint(med_axis): # сортировка линии по пикселям
    arr = med_axis
    sorted_pixels = []
    h = np.shape(arr)[0]
    w = np.shape(arr)[1]
    mask = np.array([[[255,255,255],[255,0,0],[255,255,255]],
    [[255,255,255],[255,0,255],[255,0,255]],
    [[255,255,255],[0,0,255],[255,255,255]],
    [[255,0,255],[255,0,255],[255,255,255]],
    [[255,255,0],[255,0,255],[255,255,255]],
    [[255,255,255],[255,0,255],[255,255,0]],
    [[255,255,255],[255,0,255],[0,255,255]],
    [[0,255,255],[255,0,255],[255,255,255]]])

    for y in range(1,h-1):
        for x in range(1,w-1):
            temp_area = np.array([[arr[y-1][x-1],arr[y-1][x],arr[y-1][x+1]],
                                 [arr[y][x-1],arr[y][x],arr[y][x+1]],
                                 [arr[y+1][x-1],arr[y+1][x],arr[y+1][x+1]]])
            for i in range(8):
                if np.array_equal(temp_area, mask[i]):
                    endpoint = (y,x)
                    return endpoint
    return endpoint


def sort_pixels(med_axis, endpoint):
    arr = np.copy(med_axis)
    sorted = [[endpoint[0],endpoint[1]]]
    i = 0
    while np.size(np.unique(arr)) > 1: # ищем ближайший 0 - черный
        arr[sorted[i][0],sorted[i][1]] = 255
        curr_y = sorted[i][0]
        curr_x = sorted[i][1]
        if arr[curr_y][curr_x+1] == 0:
            sorted.append([curr_y, curr_x+1])
        elif arr[curr_y+1][curr_x] == 0:
            sorted.append([curr_y+1, curr_x])
        elif arr[curr_y][curr_x-1] == 0:
            sorted.append([curr_y, curr_x-1])
        elif arr[curr_y-1][curr_x] == 0:
            sorted.append([curr_y-1, curr_x])
        elif arr[curr_y-1][curr_x+1] == 0:
            sorted.append([curr_y-1, curr_x+1])
        elif arr[curr_y+1][curr_x+1] == 0:
            sorted.append([curr_y+1, curr_x+1])
        elif arr[curr_y+1][curr_x-1] == 0:
            sorted.append([curr_y+1, curr_x-1])
        elif arr[curr_y-1][curr_x-1] == 0:
            sorted.append([curr_y-1, curr_x-1])
        i = i + 1
    return sorted


def g_codes(sorted_rdp):
    text = ['G17']
    text.append(f'G00 X{sorted_rdp[0][1]} Y{sorted_rdp[0][0]}')
    for i in range(1,len(sorted_rdp)):
        text.append(f'G01 X{sorted_rdp[i][1]} Y{sorted_rdp[i][0]}')
    return text


def gcodes_start(im):
    try:
        thresh = thresh_im(im)
        med_axis = medline(thresh)
        endpoint = find_endpoint(med_axis)
        sorted = sort_pixels(med_axis, endpoint)
        sorted_rdp = rdp(sorted, epsilon=0.7)
        text = g_codes(sorted_rdp)
        export_img = thresh

        for i in range(len(sorted_rdp)):
            export_img[sorted_rdp[i][0]][sorted_rdp[i][1]] = 255

    except (IndexError, UnboundLocalError) as e:
        text = ["Ошибка! Алгоритм не справился, простите :("]
        export_img = []
        
    return text, export_img
