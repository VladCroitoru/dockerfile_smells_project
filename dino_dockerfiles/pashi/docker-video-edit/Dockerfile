FROM ubuntu:14.04
MAINTAINER Pasi Lammi <pasi.lammi@iki.fi>
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y python-dev pkg-config libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libavresample-dev python-pip git curl imagemagick python3-scipy python-pil python-numpy
RUN pip install av
RUN pip install moviepy
RUN curl 'https://raw.githubusercontent.com/imageio/imageio-binaries/master/ffmpeg/ffmpeg.linux64' > /usr/bin/ffmpeg.linux64
RUN curl 'https://raw.githubusercontent.com/pashi/scripts/master/python/video_to_frames.py' > /usr/bin/video_to_frames.py
RUN ln -s /usr/bin/ffmpeg.linux64 /usr/bin/ffmpeg
RUN chmod +x /usr/bin/ffmpeg.linux64 /usr/bin/video_to_frames.py
RUN mkdir -p /root/.imageio/ffmpeg
RUN ln -s /usr/bin/ffmpeg.linux64 /root/.imageio/ffmpeg/ffmpeg.linux64
RUN apt-get remove -y python-dev gcc libexpat1-dev libpython-dev libpython2.7 libpython2.7-dev python2.7-dev curl
RUN mkdir /app
WORKDIR /app
