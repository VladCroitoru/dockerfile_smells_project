FROM gliderlabs/alpine:3.4

RUN apk add --no-cache mosquitto && \
	mkdir -p /etc/mosquitto/conf.d && \
	touch /etc/mosquitto/passwd

ADD custom.conf /etc/mosquitto/conf.d

EXPOSE 1883

CMD ["mosquitto"]

