FROM ubuntu:latest

ARG DEBIAN_FRONTED=noninteractive
ENV TZ=Europe/Moscow

RUN apt-get update \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && apt-get install sudo -y \
    && apt-get install wget -y \
    && apt-get install make -y \
    && apt-get install libreadline-dev -y \
    && apt-get install lib32ncurses5-dev -y \
    && apt-get install lib32z1-dev -y \
    && apt-get install vim -y \ 
    && apt-get install python3.8 -y
EXPOSE 22