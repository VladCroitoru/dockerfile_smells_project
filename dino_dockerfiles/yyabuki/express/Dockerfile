FROM ubuntu
MAINTAINER Yukimitsu Yabuki, yukimitsu.yabuki@gmail.com
RUN apt-get update && apt-get -y upgrade \
    && apt-get -y install wget \
    && wget http://bio.math.berkeley.edu/eXpress/downloads/express-1.5.1/express-1.5.1-linux_x86_64.tgz \
    && tar xvfz express-1.5.1-linux_x86_64.tgz \
    && cd express-1.5.1-linux_x86_64 \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/* \
    && cp -r /express-1.5.1-linux_x86_64/* /usr/local/bin
WORKDIR /express-1.5.1-linux_x86_64
