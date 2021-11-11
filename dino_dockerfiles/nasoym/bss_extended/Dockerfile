FROM nasoym/bash_socat_server
MAINTAINER Sinan Goo

RUN echo 'http://dl-4.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories && apk update 
RUN apk --no-cache add mongodb
RUN apk --no-cache add jq parallel 

