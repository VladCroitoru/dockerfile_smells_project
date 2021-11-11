FROM falcon8823/dpdk-docker

ARG PKTGEN_VERSION=3.1.1

RUN apt-get update -y \
  && apt-get install -y -q libpcap-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
RUN curl -O http://dpdk.org/browse/apps/pktgen-dpdk/snapshot/pktgen-${PKTGEN_VERSION}.tar.xz \
  && tar xJf pktgen-${PKTGEN_VERSION}.tar.xz -C /usr/local/src \
  && rm pktgen-${PKTGEN_VERSION}.tar.xz

WORKDIR /usr/local/src/pktgen-${PKTGEN_VERSION}
RUN make

ENV PATH "$PATH:/usr/local/src/pktgen-${PKTGEN_VERSION}/app/app/$RTE_TARGET"

CMD ['pktgen']

