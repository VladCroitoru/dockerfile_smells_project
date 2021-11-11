FROM resin/armv7hf-debian
ARG version=1.3.6.0

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get install wget && \
	wget https://dl.influxdata.com/chronograf/releases/chronograf-${version}_linux_armhf.tar.gz && \
	tar xvfz chronograf-${version}_linux_armhf.tar.gz && \
	rm chronograf-${version}_linux_armhf.tar.gz && \
	cp -av chronograf-*/* / && \
        rm -fr chronograf-* && \
	apt-get purge wget && \
	apt-get autoremove && \
	apt-get clean all && \
	rm -r /var/lib/apt/lists/*

RUN [ "cross-build-end" ]  

EXPOSE 8888
ENTRYPOINT ["/usr/bin/chronograf", "--host", "0.0.0.0", "--port", "8888", "-b", "/var/lib/chronograf/chronograf-v1.db", "-c", "/usr/share/chronograf/canned"]
