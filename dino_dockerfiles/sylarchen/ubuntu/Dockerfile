FROM ubuntu:latest
MAINTAINER Sylar Chen

# replace repo address
RUN echo "\
deb http://mirrors.sohu.com/ubuntu/ trusty main restricted universe multiverse\n\
deb http://mirrors.sohu.com/ubuntu/ trusty-security main restricted universe multiverse\n\
deb http://mirrors.sohu.com/ubuntu/ trusty-updates main restricted universe multiverse\n\
deb http://mirrors.sohu.com/ubuntu/ trusty-proposed main restricted universe multiverse\n\
deb http://mirrors.sohu.com/ubuntu/ trusty-backports main restricted universe multiverse\n\
deb-src http://mirrors.sohu.com/ubuntu/ trusty main restricted universe multiverse\n\
deb-src http://mirrors.sohu.com/ubuntu/ trusty-security main restricted universe multiverse\n\
deb-src http://mirrors.sohu.com/ubuntu/ trusty-updates main restricted universe multiverse\n\
deb-src http://mirrors.sohu.com/ubuntu/ trusty-proposed main restricted universe multiverse\n\
deb-src http://mirrors.sohu.com/ubuntu/ trusty-backports main restricted universe multiverse" > /etc/apt/sources.list

#ENV http_proxy=http://web-proxy.atl.hp.com:8080
#ENV https_proxy=https://web-proxy.atl.hp.com:8080

# update & upgrade packages
RUN apt-get update && \
apt-get upgrade -y && \
apt-get install -y curl vim wget && \
rm -rf /var/lib/apt/lists/*

# change localtime
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
