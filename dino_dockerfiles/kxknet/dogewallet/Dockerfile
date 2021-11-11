FROM ubuntu:latest
MAINTAINER ddosov.net <support@ddosov.net>
RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y curl
RUN wget https://github.com/dogecoin/dogecoin/releases/download/v1.10.0/dogecoin-1.10.0-linux64.tar.gz -O dogecoin.tar.gz
RUN tar -zxvvf dogecoin.tar.gz
RUN rm dogecoin.tar.gz
RUN mv dogecoin-1.10.0 dogecoin-bin
RUN mkdir ~/.dogecoin
RUN echo rpcuser=dogecoinrpc > ~/.dogecoin/dogecoin.conf
RUN PWord=`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 64 | head -n 1`
RUN echo rpcpassword=$PWord >> ~/.dogecoin/dogecoin.conf
CMD /dogecoin-bin/bin/dogecoind -maxconnections=500 -daemon
RUN echo Run \" tail -f ~/.dogecoin/debug.log \" to watch the download status.
EXPOSE 22555 22556
