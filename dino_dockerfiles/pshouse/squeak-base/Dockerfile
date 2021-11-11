FROM ubuntu:14.04 
RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -yq git unzip curl
RUN apt-get install -yq libc6:i386
RUN apt-get install -yq xvfb
#RUN apt-get install -yq websockify python-setuptools

# Squeak display driver
RUN apt-get install -yq libgl1-mesa-glx:i386 libxext6:i386 libsm6:i386 libice6:i386 libx11-6:i386

RUN apt-get install -y libglu1-mesa:i386 libxrender1:i386 libfreetype6:i386

#RUN apt-get install -y nginx

# setup VNC
#RUN mkdir /.vnc
#RUN x11vnc -storepasswd 1234 ~/.vnc/passwd
