FROM ravishtiwari/docker-jenkins-slave
MAINTAINER Ravish Tiwari <ravishktiwari@hotmail.com>
ENV DEBIAN_FRONTEND noninteractive
RUN echo "-- Install Node.js 8 --"
RUN apt-get update
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN apt-get install nodejs -yq \
  zip unzip \
  awscli \ 
  pkg-config 
RUN usermod -aG docker jenkins 

RUN curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose
# confirm installation
RUN add-apt-repository ppa:chris-lea/zeromq
RUN apt-get update
RUN apt-get install libzmq3-dbg libzmq3-dev libzmq3 -yq
 
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libkrb5-dev \
    pkg-config \
    libtool \
    autoconf \
    automake \
    unzip \ 
    libglib2.0-dev \
    librsvg2-dev
RUN cd /tmp && git clone git://github.com/jedisct1/libsodium.git && cd libsodium && git checkout stable && ./autogen.sh && ./configure && make check && make install && ldconfig
RUN cd /tmp && git clone --depth 1 git://github.com/zeromq/libzmq.git && cd libzmq && ./autogen.sh && ./configure && make && make install && ldconfig
RUN rm /tmp/* -rf
RUN pip install -U setuptools 
RUN pip -V && python -V
RUN apt-get install python-dev -y
#RUN npm install -g aws-sam-cli
RUN pip install aws-sam-cli 
RUN which sam
CMD ["node"]
