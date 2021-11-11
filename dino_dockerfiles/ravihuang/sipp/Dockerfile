FROM ubuntu:latest
MAINTAINER = Ravi Huang <ravi.huang@gmail.com>
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /
RUN apt-get update && \
    apt-get install -y build-essential git libssl-dev libpcap-dev libsctp-dev libncurses5-dev autoconf

RUN git clone https://github.com/SIPp/sipp.git && \
    cd sipp && \
    ./build.sh --with-pcap --with-sctp --with-openssl --with-rtpstream && \
    make install

WORKDIR /
RUN rm -rf sipp

CMD sipp
