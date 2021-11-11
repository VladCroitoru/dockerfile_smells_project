FROM resin/armv7hf-debian
ARG version=1.3.5

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get install wget && \
	wget https://dl.influxdata.com/telegraf/releases/telegraf-${version}_linux_armhf.tar.gz && \
	tar xvfz telegraf-${version}_linux_armhf.tar.gz && \
	rm telegraf-${version}_linux_armhf.tar.gz && \
	cp -av telegraf/* / && \
        rm -fr telegraf && \
	apt-get purge wget && \
	apt-get autoremove && \
	apt-get clean all && \
	rm -r /var/lib/apt/lists/*

RUN [ "cross-build-end" ]  

EXPOSE 8125 8092 8094

ENTRYPOINT ["/usr/bin/telegraf", "-config", "/etc/telegraf/telegraf.conf", "-config-directory", "/etc/telegraf/telegraf.d"]
