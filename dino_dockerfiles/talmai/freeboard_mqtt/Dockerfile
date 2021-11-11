# Pull base image
FROM node:4

RUN apt update && apt upgrade -y && \
	cd /root && \
	git clone https://github.com/Freeboard/freeboard.git && \
	cd freeboard && \
	npm install && \
	npm install paho-mqtt wget && \
	apt-get install -y vim

RUN cd /root/freeboard/plugins/ && \
	mkdir mqtt && \
	cd mqtt && \
	wget --output-document mqttws31.js https://cdnjs.cloudflare.com/ajax/libs/paho-mqtt/1.0.1/mqttws31.js

#RUN cd /root/freeboard/plugins/thirdparty/ && \
#	git clone https://github.com/alsm/freeboard-mqtt.git

RUN cd /root/freeboard/plugins/thirdparty/ && \
	mkdir freeboard-mqtt

COPY paho.mqtt.plugin.js /root/freeboard/plugins/thirdparty/freeboard-mqtt/

COPY *.json /root/freeboard/
COPY *.html /root/freeboard/

RUN mkdir /freeboard_startup
COPY run_freeboard.sh /freeboard_startup/
RUN chmod +x /freeboard_startup/*

EXPOSE 8080

WORKDIR "/root/freeboard"

ENTRYPOINT ["/freeboard_startup/run_freeboard.sh"]
CMD ["localhost", "8080"] #defaults to localhost HOST at port 8080
