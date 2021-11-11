FROM ubuntu:20.04
MAINTAINER timiil@163.com

ENV TZ=Asia/Shanghai

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential asciidoc binutils bzip2 gawk gettext git libncurses5-dev libz-dev patch unzip zlib1g-dev && \
  apt-get install -y lib32gcc1 libc6-dev-i386 subversion flex uglifyjs git-core gcc-multilib p7zip p7zip-full msmtp && \
  apt-get install -y libssl-dev texinfo libglib2.0-dev && \
  apt-get install -y rsync wget curl nano && \
  rm -rf /var/lib/apt/lists/* 
  


ENV FORCE_UNSAFE_CONFIGURE 1
