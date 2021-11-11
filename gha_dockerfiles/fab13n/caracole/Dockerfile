FROM python:3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /planet
ENV LD_LIBRARY_PATH /usr/local/lib
ENV SRC_DIR /root/src

COPY requirements-debian.txt /root/

RUN apt-get update &&\
    apt-get install -y -q $(sed -e 's/#.*$//g' /root/requirements-debian.txt) &&\
    rm -rf /var/lib/apt/lists/*

# TODO check whether libgrib-api-dev is required
RUN pip install -U pip
COPY requirements-python.txt /root/
RUN pip install -r /root/requirements-python.txt
WORKDIR /home/caracole/