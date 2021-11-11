FROM ubuntu:14.04
MAINTAINER Ge Tadeo <mr.genesis.tadeo@gmail.com>

RUN apt-get update && apt-get install -y tor
RUN echo "SocksListenAddress  0.0.0.0" >> /etc/tor/torrc

CMD ["tor"]
