FROM ubuntu:16.04
MAINTAINER Evgeniy Ozhiganov <eozhiganov@gail.com>

RUN apt-get update -qq && apt-get install -qqy \
  automake \
  libcurl4-openssl-dev \
  git \
  make \
  build-essential && \
  apt-get clean

RUN git clone --recursive https://github.com/OhGodAPet/cpuminer-multi.git

RUN cd cpuminer-multi && ./autogen.sh && ./configure CFLAGS="-O3" && make

WORKDIR /cpuminer-multi

ENTRYPOINT ["./minerd"]
