# Use Ubuntu:16.04 image as parent image
FROM ubuntu:16.04

MAINTAINER AUTHOR aggresss
ENV DEBIAN_FRONTEND noninteractive

EXPOSE 8888 
EXPOSE 6006
VOLUME /root/volume
USER root

# Modify apt-get to aliyun mirror
RUN sed -i 's/archive.ubuntu/mirrors.aliyun/g' /etc/apt/sources.list
RUN apt-get update

# Clone the docker-opencv-python repository
RUN apt-get -y install git
RUN git clone https://github.com/aggresss/docker-opencv-python.git /docker-opencv-python
WORKDIR /docker-opencv-python

# Modify timezone to GTM+8
ENV TZ=Asia/Shanghai
RUN apt-get -y install tzdata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Modify locale
RUN apt-get -y install locales
RUN locale-gen en_US.UTF-8
RUN echo "LANG=\"en_US.UTF-8\"" > /etc/default/locale && \
    echo "LANGUAGE=\"en_US:en\"" >> /etc/default/locale && \
    echo "LC_ALL=\"en_US.UTF-8\"" >> /etc/default/locale

# Install necessary library
RUN apt-get -y install apt-utils python python-dev python-pip \
    lib32z1 libglib2.0-dev libsm6 libxrender1 \
    libxext6 libice6 libxt6 libfontconfig1 libcups2 

# Modify pip mirror
RUN mkdir -p /root/.pip
RUN echo "[global]" > /root/.pip/pip.conf && \
    echo "index-url=http://mirrors.aliyun.com/pypi/simple/" >> /root/.pip/pip.conf && \
    echo "[install]" >> /root/.pip/pip.conf && \
    echo "trusted-host=mirrors.aliyun.com" >> /root/.pip/pip.conf

# Modify Jupter run arguments
RUN mkdir -p /root/.jupyter
RUN echo "# Jupyter config file" > /root/.jupyter/jupyter_config.py && \
    echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_config.py && \
    echo "c.NotebookApp.notebook_dir = u'/root/volume'" >> /root/.jupyter/jupyter_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /root/.jupyter/jupyter_config.py && \
    echo "c.NotebookApp.allow_root = True">> /root/.jupyter/jupyter_config.py && \
    echo "c.NotebookApp.port = 8888">> /root/.jupyter/jupyter_config.py && \
    echo "# default password: 12345678">> /root/.jupyter/jupyter_config.py && \
    echo "c.NotebookApp.password = u'sha1:d501736a80f9:2bf882737f5ded39b8d1803b0c3ca385325fbfa8'" >> \
    /root/.jupyter/jupyter_config.py

# Install necessary python-library
RUN pip install --upgrade pip
RUN pip install numpy scipy matplotlib pillow opencv-python ipython==5.5.0 tensorflow keras h5py
RUN pip install jupyter jupyterlab

# Make startup run file
RUN echo '#!/bin/sh' > /run.sh && \
    echo "nohup jupyter notebook" >> /run.sh
RUN chmod +x /run.sh
WORKDIR /root/volume
CMD /run.sh


