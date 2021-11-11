FROM debian:jessie
MAINTAINER RPIO
LABEL description="dockerized diamondd for running DMD Node"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
curl git build-essential less nano binutils-gold libssl-dev miniupnpc libgmp3-dev \
ca-certificates libboost-all-dev libcurl4-openssl-dev libdb5.3-dev libdb5.3++-dev && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN git clone https://github.com/dmdcoin/diamond.git /usr/src/diamond
WORKDIR /usr/src/diamond/src
RUN mkdir -p /usr/src/diamond/src/obj && \
make -f makefile.unix USE_UPNP=- && \
mv diamondd /usr/bin && \
rm -rf /usr/src/diamond

ENV HOME /diamond

ADD ./bin /usr/local/bin
RUN chmod a+x /usr/local/bin/*

VOLUME ["/diamond"]
EXPOSE 17771 17772
WORKDIR /diamond

CMD ["dmd_oneshot"]
