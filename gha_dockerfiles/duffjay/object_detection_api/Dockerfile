# CUDA 11.2.2  cuDNN 8  Ubuntu 20.04
# - expecting nvidia-docker
#
# docker build -t object_detection_api:tf25 .
#
# assumes
# - you have awscli installed on the host such that you can copy credientials & config files
# /project 
#   /opencv
#   /opencv_contrib

FROM nvidia/cuda:11.2.2-cudnn8-devel-ubuntu20.04

WORKDIR /app

# this will eliminate interactive dialog on installation steps
ARG DEBIAN_FRONTEND=noninteractive
ARG X11_COOKIE=none
ARG USER_PASSWORD=none
ARG AWS_KEY=default
ARG AWS_SECRET=default
ARG AWS_REGION=us-east-1
ARG AWS_OUTPUT=json

LABEL author=jduff

ENV user jay
ENV group duff

# --- user: root
RUN apt-get update && apt-get install -y apt-utils 
RUN apt-get install -y sudo
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata

# installing gedit - very problematic!!! 
# RUN sudo apt-get install -y gedit

# add user
RUN useradd -m -d /home/${user} ${user} && \
    chown -R ${user} /home/${user} && \
    adduser ${user} sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers


# --- user: jay

USER ${user}
WORKDIR /home/${user}

# Install apt dependencies
RUN sudo apt-get update 
RUN sudo apt-get install -y \
    nano \
    git \
    gpg-agent \
    python3-cairocffi \
    protobuf-compiler \
    python3-pil \
    python3-lxml \
    python3-tk \
    wget
   

    
RUN sudo apt-get install -y software-properties-common
RUN sudo add-apt-repository ppa:deadsnakes/ppa
RUN sudo apt-get update
RUN sudo apt-get install -y apt-utils
RUN sudo apt-get install -y pigz
RUN sudo apt-get install -y awscli


#RUN DEBIAN_FRONTEND=noninteractive sudo apt-get install keyboard-configuration
RUN sudo apt-get install -y libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

# gstreamer
# this is BEFORE Anacoda
RUN sudo apt-get install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev 
RUN sudo apt-get install -y gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly 
RUN sudo apt-get install -y gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl 
RUN sudo apt-get install -y gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio



# part of the opencv build process
# - includes all of the gstreamer stuff
# Install required libraries
RUN sudo apt-get install -y build-essential cmake pkg-config unzip yasm git checkinstall
RUN sudo apt-get install -y libjpeg-dev libpng-dev libtiff-dev
RUN sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libavresample-dev 
RUN sudo apt-get install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev 
RUN sudo apt-get install -y libxvidcore-dev x264 libx264-dev libfaac-dev libmp3lame-dev libtheora-dev  
RUN sudo apt-get install -y libfaac-dev libmp3lame-dev libvorbis-dev

RUN sudo apt-get install -y libopencore-amrnb-dev libopencore-amrwb-dev

RUN sudo apt-get install -y libdc1394-22 libdc1394-22-dev libxine2-dev libv4l-dev v4l-utils 
RUN cd /usr/include/linux 
RUN ln -s -f ../libv4l1-videodev.h videodev.h 
#RUN cd ~
RUN sudo apt-get install -y libgtk-3-dev

# C++ Parallellism
RUN sudo apt-get install -y libtbb-dev
# Optimization
RUN sudo apt-get install -y libatlas-base-dev gfortran

# Optional
RUN sudo apt-get install -y libprotobuf-dev protobuf-compiler 
RUN sudo apt-get install -y libgoogle-glog-dev libgflags-dev 
RUN sudo apt-get install -y libgphoto2-dev libeigen3-dev libhdf5-dev doxygen

# access python 3.9 with $ python3.9
RUN sudo apt-get install -y python3.7
RUN sudo apt-get install -y python3.9
RUN sudo apt-get install -y python3-pip
RUN sudo apt-get install -y python-dev
RUN sudo apt-get install -y python3-dev
RUN sudo apt-get install -y python3.7-dev
RUN sudo apt-get install -y python3.8-dev
RUN sudo apt-get install -y python3.9-dev
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get install -y python3-setuptools
RUN sudo apt-get install -y python3-testresources


# you should be at python 3.8 only
RUN sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
RUN sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2
RUN sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 3
RUN sudo update-alternatives  --set python /usr/bin/python3.8


RUN python -m pip install --upgrade pip

# -- UI forwarding via X11 -- 
# ** accompish this with movuting a volume for Xauthority
# https://www.geeksforgeeks.org/running-gui-applications-on-docker-in-linux/
# you need to put in the correct X11_COOKIE - per computer
# RUN sudo apt-get install -y xauth
# RUN touch ~/.Xauthority
# RUN xauth add 5950X/unix:  MIT-MAGIC-COOKIE-1  b60ae6f2a270b8d52b581154d0a06a00

EXPOSE 8887



# -- aws config --
#RUN aws configure set aws_access_key_id $AWS_KEY
RUN aws configure set aws_access_key_id ${AWS_KEY} --profile jmduff
RUN aws configure set aws_secret_access_key ${AWS_SECRET} --profile jmduff 
RUN aws configure set region ${AWS_REGION} --profile jmduff


# install Anaconda
RUN wget -O install_anaconda.sh https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
RUN bash install_anaconda.sh -bu
RUN ./anaconda3/bin/conda config --set auto_activate_base false
RUN ./anaconda3/bin/conda create -y -n od_tf25 python=3.8


# Make RUN commands use the new environment:
# - https://pythonspeed.com/articles/activate-conda-dockerfile/
# - https://stackoverflow.com/questions/55123637/activate-conda-environment-in-docker

# Make RUN commands use the new environment:
RUN echo "export PATH=$PATH:/home/$user/anaconda3/bin" >> ~/.bashrc
RUN echo "conda init bash" >> ~/.bashrc
#RUN /home/$user/anaconda3/bin/conda init
RUN echo "source activate od_tf25" >> ~/.bashrc
# SHELL ["/bin/bash", "--login", "-c"]

SHELL ["/bin/sh","-c"]
RUN echo $CONDA_DEFAULT_ENV
RUN echo $CONDA_PREFIX

# pip install pre-requisites
#RUN pip install numpy  # v1.21.2

RUN echo "*** finished - /project/docker/object_detection_api$ bash ./post_build.sh"

## *** do the conda init in the build opencv script **
SHELL ["/bin/sh", "-c"]
