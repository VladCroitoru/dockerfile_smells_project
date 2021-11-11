from ubuntu:14.04

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y python gcc make g++ wget

RUN wget https://nodejs.org/download/rc/v4.0.0-rc.1/node-v4.0.0-rc.1.tar.gz \
    && tar -zxvf node-v4.0.0-rc.1.tar.gz \
    && cd node-v4.0.0-rc.1 \
    && ./configure \
    && make install 

RUN apt-get install -y openjdk-7-jdk
RUN wget http://static.imply.io/release/imply-1.0.0.tar.gz \
    && tar zxvf imply-1.0.0.tar.gz \
    && cd imply-1.0.0

ENTRYPOINT ["/imply-1.0.0/bin/supervise"]
CMD ["-c", "/imply-1.0.0/conf/supervise/quickstart.conf"]
