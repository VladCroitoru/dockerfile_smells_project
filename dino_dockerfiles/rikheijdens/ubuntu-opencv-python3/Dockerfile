# Dockerfile to build OpenCV 3.3.0 with Python3 and ffmpeg support.
FROM ubuntu:xenial
MAINTAINER Rik Heijdens

COPY install_opencv.sh /tmp
WORKDIR /tmp
RUN apt-get update \
  && chmod +x install_opencv.sh \
  && ./install_opencv.sh 3.3.0 \
  && apt-get remove -y build-essential cmake git curl \
  && apt-get clean -y \
  && apt-get autoclean -y \
  && apt-get autoremove -y
