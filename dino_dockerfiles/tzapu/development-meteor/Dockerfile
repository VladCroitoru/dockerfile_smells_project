FROM node:4.8.3
MAINTAINER Alex T<alex@tzapu.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && apt-get install -y locales -qq && locale-gen en_US.UTF-8 en_us && dpkg-reconfigure locales && locale-gen C.UTF-8 && /usr/sbin/update-locale LANG=C.UTF-8
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

#RUN ln -s /usr/local/bin/node /usr/local/bin/nodejs
RUN curl -sL https://install.meteor.com/?release=1.4.4.3  | sed s/--progress-bar/-sL/g | /bin/sh
