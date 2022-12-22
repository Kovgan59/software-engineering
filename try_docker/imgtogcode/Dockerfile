FROM python:3.10.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

EXPOSE 5000
CMD ["python3", "g_codes_web.py"]