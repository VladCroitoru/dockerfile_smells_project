FROM ubuntu:16.04
MAINTAINER Sreekanth G S <mail@sreekanth.in>

WORKDIR /root

RUN apt-get update && apt-get install -y wget && \
    wget https://download.litecoin.org/litecoin-0.15.1/linux/litecoin-0.15.1-x86_64-linux-gnu.tar.gz && \
    tar -zvxf litecoin-0.15.1-x86_64-linux-gnu.tar.gz && \
    mv litecoin-0.15.1 litecoin && \
    cp litecoin/bin/* /usr/local/bin

VOLUME ["/opt/litecoin"]

EXPOSE 9332

CMD ["litecoind", "--conf=/opt/litecoin/litecoin.conf", "--printtoconsole"]
