# pull the official base image
FROM ubuntu:latest
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
# install dependencies
# copy project
COPY . /usr/src/app 
RUN apt-get update && apt-get install -y tesseract-ocr libpoppler-cpp-dev mupdf default-jre default-jdk python3-pip build-essential pkg-config python-dev && rm -rf /var/lib/apt/lists/* && apt autoremove && pip3 install -r requirements.txt
#RUN pip3 install virtualenv
#RUN python3 -m virtualenv env
#RUN source env/bin/activate


EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# 
# Command line to activate docker
# docker build --tag django_demo:latest .
# docker run --name django_demo -d -p 8000:8000 django_demo:latest
# ffmpeg libsm6 libxext6 build-essential pkg-config python-dev >> Add these in case build or anything else fails
