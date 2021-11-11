#Comments
From nginx:1.11

MAINTAINER Patrick Bailey "pbailey@10x13.com"

ENV PATS_ENV "Our Docker Class"

RUN apt-get update
RUN apt-get install -y \
         git \
         vim \
         tree 
RUN apt-get install -y htop

EXPOSE 9090

COPY default.conf /etc/nginx/conf.d/default.conf
