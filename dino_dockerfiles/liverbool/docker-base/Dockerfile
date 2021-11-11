FROM debian:wheezy

MAINTAINER  Liverbool "nukboon@gmail.com"

#ENV DEBIAN_FRONTEND noninteractive

RUN echo 'Asia/Bangkok' | tee /etc/timezone

RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup
RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache

RUN apt-get update -y --fix-missing
#RUN apt-get install supervisor -y
