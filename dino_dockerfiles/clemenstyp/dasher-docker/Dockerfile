FROM   ubuntu:latest
MAINTAINER	Clemens Putschli <clemens@putschli.de>

#Install libpcap-dev
RUN \
    sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get -y upgrade && \
     apt-get install -y sudo && \
    apt-get install -y libpcap-dev && \
    apt-get install -y git && \
    apt-get install -y nodejs && \
    apt-get install -y npm && \
    apt-get install nodejs-legacy && \ 
    apt-get clean && rm -rf /var/lib/apt/lists/*

#install dasher
RUN cd /root && export GIT_SSL_NO_VERIFY=1 && \
    git config --global http.sslVerify false && \
    git clone https://github.com/maddox/dasher.git

WORKDIR /root/dasher
RUN cd /root/dasher && npm install
ADD config.json /root/dasher/config.json

# Interface the environment
VOLUME /root/dasher/config

# Baseimage init process
CMD cd /root/dasher && cp -n config.json /root/dasher/config/config.json  && npm run start
