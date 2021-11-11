FROM ubuntu:latest
MAINTAINER truthadjustr@gmail.com
LABEL description="nodejs 5.x and zmq support because nodejs 6.x has nan error"

RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates \
    build-essential \
    net-tools \
    wget \
    curl \
    git \
    libtool \
    autoconf \
    automake \
    pkg-config \
    python \
    tmux \
    vim-tiny \
    python-pip \
    tcpdump \
    python-setuptools \
    && curl -sL https://deb.nodesource.com/setup_5.x | bash - \
    && apt-get install -y nodejs \
    && git clone https://github.com/zeromq/libzmq \
    && cd libzmq \
    && mkdir -p /root/testapps/zmq/ \
    && mkdir -p /root/testapps/rabbitmq/client/ \
    && ./autogen.sh && ./configure && make && make install && ldconfig && cd / \
    && npm install zmq \
    && pip install zmq \
    && pip install pika \
    && npm install amqplib \
    && git clone https://github.com/jimbojw/node-zmq-talk.git /root/testapps/zmq/node-zmq-talk/ \
    && wget https://gist.githubusercontent.com/carlhoerberg/006b01ac17a0a94859ba/raw/907252549bf711ffa16a05bb8b7f2bdf2937e7f2/reconnect.js -O /root/testapps/rabbitmq/client/reconnect.js

COPY dotbashrc /root/.bashrc
COPY dottmux.conf /root/.tmux.conf
COPY welcome.ascii /etc/
