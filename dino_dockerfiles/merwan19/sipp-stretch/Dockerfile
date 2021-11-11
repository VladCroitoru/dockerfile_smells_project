FROM debian:stretch

MAINTAINER Merwan Ouddane
ENV SIPP_VERSION 3.5.1

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential curl automake ncurses-dev libsctp-dev libpcap-dev libssl1.0-dev

RUN mkdir /build /data && \
    cd /build && \
    curl -sqLkv https://github.com/SIPp/sipp/releases/download/v${SIPP_VERSION}/sipp-${SIPP_VERSION}.tar.gz | tar xvzf - --strip-components=1
	
RUN cd /build && \
    ./build.sh --with-openssl --with-pcap --with-rtpstream --with-sctp && \
    mv sipp /usr/bin
