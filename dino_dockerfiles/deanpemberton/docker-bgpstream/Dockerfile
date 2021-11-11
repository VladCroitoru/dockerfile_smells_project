FROM ubuntu
MAINTAINER Dean Pemberton

WORKDIR /tmp
RUN apt-get update && apt-get install -y wget build-essential  zlib1g-dev libbz2-dev libcurl4-openssl-dev && rm -rf /var/lib/apt/lists/* && \
wget http://research.wand.net.nz/software/wandio/wandio-1.0.3.tar.gz && \
tar xvzf wandio-1.0.3.tar.gz && \
cd wandio-1.0.3 && ./configure --prefix=/usr &&  make && make install  && ldconfig 
WORKDIR /tmp
RUN wget http://bgpstream.caida.org/bundles/caidabgpstreamwebhomepage/dists/bgpstream-1.1.0.tar.gz && \
tar xvzf bgpstream-1.1.0.tar.gz && \
cd bgpstream-1.1.0 && ./configure --prefix=/usr &&  make && make check && make install && ldconfig
WORKDIR /data

ENTRYPOINT ["bgpreader"]
CMD ["--help"]
