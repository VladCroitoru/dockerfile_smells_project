FROM ubuntu:xenial
MAINTAINER miguel.bernadin@gmail.com

RUN apt-get update && \
apt-get install -y \
default-jre \
default-jdk \
curl \
python \
python-pip \
virtualenv
RUN curl https://downloads.dcos.io/binaries/cli/linux/x86-64/dcos-1.9/dcos > /usr/local/bin/dcos 
RUN chmod +x /usr/local/bin/dcos 
