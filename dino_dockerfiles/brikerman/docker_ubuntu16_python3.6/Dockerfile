# Version: 5.0
# Name: Python3.6

FROM ubuntu:16.04
MAINTAINER BrikerMan "https://github.com/BrikerMan/"

USER root

RUN rm -rf /etc/apt/sources.list
RUN echo "deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted \ndeb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted \ndeb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial universe \ndeb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates universe \ndeb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial multiverse \ndeb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates multiverse \ndeb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse \ndeb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted \ndeb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security universe \ndeb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security multiverse" >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv

# Install necessary tools
RUN apt-get install -y git
RUN apt-get install -y language-pack-en-base
RUN apt-get install -y locales
RUN apt-get install -y nano wget dialog net-tools iputils-ping
RUN apt-get install -y pandoc
RUN apt install tzdata

# prepare nginx
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y nginx-full
RUN rm -rf /etc/nginx/sites-enabled/default

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# update pip & python
RUN pip3 install wheel
RUN pip3 install ipython
RUN pip3 install --upgrade pip
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y libpcre3 libpcre3-dev
