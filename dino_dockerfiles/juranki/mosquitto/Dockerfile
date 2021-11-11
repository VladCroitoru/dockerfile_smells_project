FROM alpine:3.6

RUN apk --no-cache add supervisor dcron certbot mosquitto=1.4.12-r0

RUN mkdir /mosquitto_data && chown mosquitto:mosquitto /mosquitto_data

COPY mosquitto.conf /etc/mosquitto/mosquitto.conf
COPY supervisord.conf /etc/supervisord.conf

CMD supervisord -c /etc/supervisord.conf
