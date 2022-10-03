from tkinter import *
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import pandas as pd


class GetFile:
    
    file_path = ""
    file_name = ""
    
    
    def get_filepath(self):
        global file_path
        root = Tk()
        root.overrideredirect(True)
        root.attributes("-alpha", 0)
        file_path = askopenfilename()
        root.destroy()
        return file_path


    def get_filename(self):
        global file_path
        global file_name
        if file_path == "":
            file_path = self.get_filepath(self)
        file_name = file_path.split("/")[-1]
        return file_name
    
    
class GetData(GetFile):

    def import_data_matrix(self, file_path = 0):
        data_mat = []
        if file_path == 0:
            file_path = self.get_filepath()
        f = open(file_path, 'r')
        for line in f:
            row = line.split()
            row = [float(x) for x in row]
            data_mat.append(row)
        return data_mat
    
    
    def import_data_rows(self, data_mat = 0):
        if data_mat == 0:
            data_mat = self.import_data_matrix(self)
        data_x = []
        data_y = []
        n = len(data_mat)
        for i in range(n): 
            data_x.append(data_mat[i][0])
            data_y.append(data_mat[i][1])
        return [data_x, data_y]
        
    
class BuildGraph(GetData):

    def build_graph(self, data):
        df = pd.DataFrame({'Time': data[0], 'Data': data[1]})
        df.plot.line(y='Data', x='Time')


File = BuildGraph()
file_path = File.get_filepath()
print(file_path)
file_name = File.get_filename()
print(file_name)
data_mat = File.import_data_matrix(file_path)
print(data_mat)
data = File.import_data_rows(data_mat)
print(data)
File.build_graph(data)