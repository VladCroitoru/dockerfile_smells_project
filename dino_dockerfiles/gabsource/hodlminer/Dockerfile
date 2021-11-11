#
# Dockerfile for cpuminer
# usage: docker run creack/cpuminer --url xxxx --user xxxx --pass xxxx
# ex: docker run creack/cpuminer --url stratum+tcp://ltc.pool.com:80 --user creack.worker1 --pass abcdef
#
#

FROM            ubuntu:14.04
MAINTAINER      Guillaume J. Charmes <guillaume@charmes.net>

RUN             apt-get update -qq && \
                apt-get install -qqy automake libcurl4-openssl-dev git make

RUN             git clone https://github.com/wolf9466/hodlminer-wolf

RUN             cd hodlminer-wolf && \
                ./autogen.sh && \
                ./configure CFLAGS="-O3" && \
                make

ADD		start-mining.sh hodlminer-wolf/start-mining.sh

ENV		HODL_URL	stratum+tcp://hodl.suprnova.cc:4693
ENV		HODL_USERNAME	MyUsername
ENV		HODL_WORKER	MyWorker
ENV		HODL_PASSWORD	password

WORKDIR         /hodlminer-wolf
ENTRYPOINT      ["./start-mining.sh"]
