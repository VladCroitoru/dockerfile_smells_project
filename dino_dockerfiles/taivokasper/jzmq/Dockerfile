FROM taivokasper/nodejs:latest

MAINTAINER Taivo Käsper <taivo.kasper@gmail.com>

RUN apt-get update -y
RUN apt-get install -y build-essential make pkg-config libtool libtool-bin autoconf automake curl \
    bzip2 libfreetype6 libfontconfig1

WORKDIR /opt

RUN curl http://download.zeromq.org/zeromq-4.0.5.tar.gz -o /opt/zeromq-4.0.5.tar.gz && \
    tar -zxf zeromq-4.0.5.tar.gz && \
    rm zeromq-4.0.5.tar.gz

WORKDIR /opt/zeromq-4.0.5

RUN ./configure && \
    make && \
    make install && \
    ldconfig

WORKDIR /opt

RUN rm -rf zeromq-4.0.5

RUN curl -L https://github.com/zeromq/jzmq/archive/v3.1.0.tar.gz -o /opt/jzmq-3.1.0.tar.gz && \
    tar -zxf jzmq-3.1.0.tar.gz && \
    rm jzmq-3.1.0.tar.gz

WORKDIR /opt/jzmq-3.1.0

RUN ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    ldconfig

WORKDIR /opt

RUN rm -rf jzmq-3.1.0

RUN apt-get remove -y build-essential make pkg-config libtool autoconf automake curl && \
    apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV LD_LIBRARY_PATH /usr/local/lib

WORKDIR /root
