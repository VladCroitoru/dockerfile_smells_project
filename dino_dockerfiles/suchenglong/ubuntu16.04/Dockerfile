FROM ubuntu:16.04

RUN apt-get update \
    && apt-get -y install curl wget git vim language-pack-zh-hans language-pack-zh-hans-base
    
RUN locale-gen zh_CN.UTF-8
ENV LANG zh_CN.UTF-8
ENV LANGUAGE zh_CN:zh
ENV TZ Asia/Shanghai
RUN echo "alias ls='ls --color=auto'" >> /root/.bashrc
    
RUN apt-get -y install \
    make \
    python2.7 \
    python-pip \
    python-dev \
    python3.5 \
    python3-pip \
    python3.5-dev 






