FROM ubuntu:latest
MAINTAINER Yukimitsu Yabuki, yukimitsu.yabuki@gmail.com
RUN apt-get update && apt-get -y upgrade \
    && apt-get -y install wget \
    && wget -O salmon.tar.gz https://github.com/COMBINE-lab/salmon/releases/download/v0.8.2/Salmon-0.8.2_linux_x86_64.tar.gz \
    && tar xvfz salmon.tar.gz \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*
ENV PATH $PATH:/Salmon-0.8.2_linux_x86_64/bin
WORKDIR /Salmon-0.8.2_linux_x86_64
