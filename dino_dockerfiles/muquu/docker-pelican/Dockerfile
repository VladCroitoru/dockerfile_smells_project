FROM ubuntu:16.04
MAINTAINER muquu <muquu@skytrum.com>

# Japan mirror for local build
# RUN echo "deb http://jp.archive.ubuntu.com/ubuntu/ xenial main restricted\n\
# deb-src http://jp.archive.ubuntu.com/ubuntu/ xenial main restricted\n\
# deb http://jp.archive.ubuntu.com/ubuntu/ xenial-updates main restricted\n\
# deb-src http://jp.archive.ubuntu.com/ubuntu/ xenial-updates main restricted\n\
# deb http://jp.archive.ubuntu.com/ubuntu/ xenial universe\n\
# deb-src http://jp.archive.ubuntu.com/ubuntu/ xenial universe\n\
# deb http://jp.archive.ubuntu.com/ubuntu/ xenial-updates universe\n\
# deb-src http://jp.archive.ubuntu.com/ubuntu/ xenial-updates universe\n\
# deb http://jp.archive.ubuntu.com/ubuntu/ xenial multiverse\n\
# deb-src http://jp.archive.ubuntu.com/ubuntu/ xenial multiverse\n\
# deb http://jp.archive.ubuntu.com/ubuntu/ xenial-updates multiverse\n\
# deb-src http://jp.archive.ubuntu.com/ubuntu/ xenial-updates multiverse\n\
# deb http://jp.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse\n\
# deb-src http://jp.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse\n\
# deb http://security.ubuntu.com/ubuntu xenial-security main restricted\n\
# deb-src http://security.ubuntu.com/ubuntu xenial-security main restricted\n\
# deb http://security.ubuntu.com/ubuntu xenial-security universe\n\
# deb-src http://security.ubuntu.com/ubuntu xenial-security universe\n\
# deb http://security.ubuntu.com/ubuntu xenial-security multiverse\n\
# deb-src http://security.ubuntu.com/ubuntu xenial-security multiverse\n"> /etc/apt/sources.list

# Set various options
USER root
WORKDIR /root

# Update OS
RUN apt-get update && \
    apt-get full-upgrade -y && \
    apt-get autoremove -y && \
    apt-get autoclean -y

# Install require packages
RUN apt-get install -y \
    locales \
    locales-all \
    language-pack-ja \
    git \
    zip \
    curl \
    pngquant \
    libjpeg-progs \
    build-essential \
    python3-dev \
    python3-pip

# Fix locale
RUN locale-gen ja_JP.UTF-8
RUN update-locale
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
RUN ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
