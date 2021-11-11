FROM ubuntu:20.04

RUN apt update

RUN apt install -y zip

RUN apt install -y unzip

RUN apt install -y curl

RUN apt install -y nano

RUN apt install -y vim

RUN apt update

COPY . /home

WORKDIR /home

RUN mkdir test

RUN apt update