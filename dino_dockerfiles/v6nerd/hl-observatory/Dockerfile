FROM ubuntu:trusty-20190515
MAINTAINER v6nerd
RUN apt-get update && apt-get install -y curl git python3 python3.4 python3-setuptools python3-pip 
RUN pip3 install flask daemonize rsa requests
RUN mkdir /var/log/hl-observatory
RUN git clone https://github.com/rkokkelk/hl-observatory/
WORKDIR /hl-observatory
RUN mkdir ./results
