FROM debian:jessie

ENV TS_VERSION "trafficserver-7.1.1"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
	wget \
	bzip2 \
	build-essential \
	libssl-dev \
	tcl-dev \
	libxml2-dev \
	libpcre3-dev \
  libcurl3 \
  libncurses5-dev \
	ssl-cert

RUN wget "http://www-eu.apache.org/dist/trafficserver/$TS_VERSION.tar.bz2" && \
    tar xjf $TS_VERSION.tar.bz2 && \
    rm $TS_VERSION.tar.bz2 && \
    cd $TS_VERSION && \
    ./configure --prefix=/opt/trafficserver && \
    make && \
    make install

RUN ldconfig

# Run regression testing
RUN /opt/trafficserver/bin/traffic_server -R 1

EXPOSE 80

CMD /opt/trafficserver/bin/traffic_server
