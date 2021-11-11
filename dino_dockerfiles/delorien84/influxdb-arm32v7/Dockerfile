FROM resin/armv7hf-debian
ARG version=1.3.2

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get install wget && \
	wget https://dl.influxdata.com/influxdb/releases/influxdb-${version}_linux_armhf.tar.gz && \
	tar xvfz influxdb-${version}_linux_armhf.tar.gz && \
	rm influxdb-${version}_linux_armhf.tar.gz && \
	cp -av influxdb-*/* / && \
        rm -fr influxdb-* && \
	apt-get purge wget && \
	apt-get autoremove && \
	apt-get clean all && \
	rm -r /var/lib/apt/lists/*

RUN [ "cross-build-end" ]  

EXPOSE 8086
ENTRYPOINT ["/usr/bin/influxd"]

