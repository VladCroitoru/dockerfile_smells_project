#!/usr/bin/env bash
# docker-deforestprob

# Base image
FROM debian:stretch
MAINTAINER Ghislain Vieilledent <ghislain.vieilledent@cirad.fr>

# Terminal
ENV TERM=xterm
ENV LC_ALL C.UTF-8

# Proxy
#ENV PROXY="http://10.168.209.73:8012"
#RUN export http_proxy=$PROXY
#RUN export https_proxy=$PROXY
#RUN export ftp_proxy=$PROXY
#RUN echo "Acquire::http::proxy \""$PROXY"\";" >> /etc/apt/apt.conf
#RUN echo "Acquire::https::proxy \""$PROXY"\";" >> /etc/apt/apt.conf
#RUN echo "Acquire::ftp::proxy \""$PROXY"\";" >> /etc/apt/apt.conf

# Install debian packages with apt-get
ADD apt-packages.txt /tmp/apt-packages.txt
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get dist-upgrade -y \
    && xargs -a /tmp/apt-packages.txt apt-get install -y

# Install Google Cloud SDK
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-stretch main" >> /etc/apt/sources.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt-get update && apt-get install -y google-cloud-sdk google-cloud-sdk-app-engine-python

# Reconfigure locales
RUN dpkg-reconfigure locales \
    && locale-gen C.UTF-8 \
    && /usr/sbin/update-locale LANG=C.UTF-8 \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && dpkg-reconfigure locales

# Clean-up
RUN apt-get autoremove -y \
    && apt-get clean -y

# Install python packages with pip
ADD /requirements/ /tmp/requirements/
RUN pip install --upgrade pip \
    && pip install -r /tmp/requirements/pre-requirements.txt \
    && pip install -r /tmp/requirements/requirements.txt \
    && pip install --upgrade https://github.com/ghislainv/deforestprob/archive/master.zip
#RUN pip install --proxy $PROXY -r /tmp/requirements/additional-reqs.txt

# Create user
RUN useradd --create-home --home-dir /home/dockeruser --shell /bin/bash dockeruser \
    && adduser dockeruser sudo \
    && echo "dockeruser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
# Create home with script
ADD run_ipython.sh /home/dockeruser
RUN chmod +x /home/dockeruser/run_ipython.sh \
    && chown dockeruser /home/dockeruser/run_ipython.sh

# Prepare notebook
EXPOSE 8888
USER dockeruser
RUN mkdir -p /home/dockeruser/deforestprob
ENV HOME=/home/dockeruser
ENV SHELL=/bin/bash
ENV USER=dockeruser
VOLUME /home/dockeruser/deforestprob
WORKDIR /home/dockeruser/deforestprob

# Run jupyter notebook
CMD ["/home/dockeruser/run_ipython.sh"]

# End
