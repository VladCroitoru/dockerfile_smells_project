FROM ubuntu:16.04

MAINTAINER <panther93@protonmail.com>



WORKDIR /root

RUN apt update

RUN apt-get install -y wget

RUN wget https://github.com/dogecoin/dogecoin/releases/download/v1.10.0/dogecoin-1.10.0-linux64.tar.gz

RUN tar -zvxf dogecoin-1.10.0-linux64.tar.gz

RUN mv dogecoin-1.10.0 dogecoin

RUN cp dogecoin/bin/* /usr/local/bin



VOLUME ["/opt/dogecoin"]



EXPOSE  8332 18332 22556 44556


CMD ["dogecoind", "--conf=/opt/dogecoin/dogecoin.conf", "--printtoconsole"]