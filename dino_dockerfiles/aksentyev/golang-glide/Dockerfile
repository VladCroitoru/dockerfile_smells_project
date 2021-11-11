FROM golang

LABEL maintainer "grigory.aksentiev@gmail.com"

RUN apt update 
RUN apt install -y golang-glide
RUN apt clean
RUN mkdir -p /root/.ssh
RUN printf 'Host bitbucket.org\n  StrictHostKeyChecking no\n' > /root/.ssh/config
