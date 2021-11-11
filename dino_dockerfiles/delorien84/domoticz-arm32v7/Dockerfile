FROM resin/armv7hf-debian:stretch

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get install wget python3.5 python3.5-dev libusb-0.1-4 libssl1.0.2 && \
    mkdir -p /opt/domoticz && \
    cd /opt/domoticz && \
	wget https://releases.domoticz.com/releases/release/domoticz_linux_armv7l.tgz && \
	tar xvfz domoticz_linux_armv7l.tgz && \
	rm domoticz_linux_armv7l.tgz && \
	apt-get purge wget && \
	apt-get autoremove && \
	apt-get clean all && \
	rm -r /var/lib/apt/lists/* && \
	mkdir -p /var/domoticz && \
	mkdir -p /var/log

RUN [ "cross-build-end" ]  

EXPOSE 8080
ENTRYPOINT ["/opt/domoticz/domoticz"]
CMD ["-www", "8080", "-dbase", "/var/domoticz/domoticz.db", "-log", "/var/log/domoticz.log", "-loglevel", "1"]

