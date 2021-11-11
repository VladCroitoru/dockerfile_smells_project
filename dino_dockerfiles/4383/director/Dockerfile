############################################
# director v0.1
# author: Hervé Beraud
# url: https://github.com/4383/director
############################################
FROM ubuntu:latest
RUN \
  apt-get update && \
  apt-get -y upgrade

RUN \
  apt-get -y install libcurl4-gnutls-dev && \
  apt-get -y install tor && \
  apt-get -y install proxychains && \
  apt-get -y install git

RUN cd /usr/bin && git clone https://github.com/4383/dirb
RUN apt-get -y install gcc && apt-get -y install make

RUN cd /usr/bin/dirb && ./configure && make && chmod 777 -R .
RUN mkdir -p /usr/share/dirb/wordlists && cp -R /usr/bin/dirb/wordlists/* /usr/share/dirb/wordlists
RUN apt-get -y install polipo

ENV TARGET=127.0.0.1
ENV DIRBPROTO="http://"

CMD \
    service tor start && \
    service polipo start && \
    proxychains /usr/bin/dirb/dirb $DIRBPROTO$TARGET /usr/bin/dirb/wordlists/common.txt
