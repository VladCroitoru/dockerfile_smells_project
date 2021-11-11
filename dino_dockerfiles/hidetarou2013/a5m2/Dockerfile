FROM ubuntu:14.04 
MAINTAINER hidetarou2013 "hide1227@gmail.com" 
RUN dpkg --add-architecture i386
RUN apt-get update 
RUN apt-get install -y unzip 
RUN apt-get install -y software-properties-common && add-apt-repository -y ppa:ubuntu-wine/ppa
RUN apt-get update -y
RUN apt-get install -y wine1.7 winetricks xvfb
RUN apt-get purge -y software-properties-common
RUN apt-get autoclean -y
ADD a5m2_2.11.4_x64.zip /usr/local/bin/
WORKDIR /usr/local/bin
RUN unzip a5m2_2.11.4_x64.zip
WORKDIR /
CMD wine /usr/local/bin/A5M2.exe