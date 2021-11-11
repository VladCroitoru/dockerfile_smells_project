FROM ubuntu:trusty

RUN apt-get update && \
    apt-get install -y build-essential libopencv-dev python-opencv

WORKDIR /usr/src/app

COPY ./src /usr/src/app/src
COPY ./include /usr/src/app/include
COPY ./examples /usr/src/app/examples
COPY ./Makefile /usr/src/app

RUN sed -i '3s/OPENCV=0/OPENCV=1/' Makefile && \
    make

VOLUME /usr/src/app/weights
COPY . /usr/src/app
