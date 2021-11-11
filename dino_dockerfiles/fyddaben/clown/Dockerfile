FROM node:4

MAINTAINER fyddaben <838730592@qq.com>

RUN apt-get update && apt-get install -y unzip bash vim && apt-get update && apt-get install -qq libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ yasm && echo "79.124.17.100 www.ffmpeg.org" >> /etc/hosts

RUN cd /home && wget https://www.ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2 && tar jxvf ffmpeg-snapshot.tar.bz2 && cd ffmpeg && ./configure --prefix=/usr &&  make -j 8  

RUN mkdir -p /home/work/video  

RUN cd /home/work &&  wget https://github.com/fyddaben/clown/archive/master.zip && unzip master.zip && cd clown-master/app  && npm i 


WORKDIR  /home/work/clown-master
