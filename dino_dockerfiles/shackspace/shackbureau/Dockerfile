FROM ubuntu:16.04
MAINTAINER shackspace

EXPOSE 8000

ENV DEBIAN_FRONTEND noninteractive

USER root
RUN apt-get update -y && apt-get install -y python3-pip\
    zlib1g-dev\
    libjpeg8-dev\
    lib32z1-dev\
    postgresql-server-dev-all\
    git\
    postgresql-client\
    libfreetype6-dev\
    curl\
    locales

RUN apt-get install --no-install-recommends -y \
    texlive\
    texlive-latex-extra\
    lmodern\
    texlive-lang-german

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ADD requirements.txt /opt/code/requirements.txt
WORKDIR /opt/code
RUN pip3 install -Ur requirements.txt
ADD . /opt/code

RUN useradd uid1000 -d /home/uid1000
RUN mkdir -p /home/uid1000 && chown uid1000: /home/uid1000

USER uid1000

WORKDIR shackbureau
