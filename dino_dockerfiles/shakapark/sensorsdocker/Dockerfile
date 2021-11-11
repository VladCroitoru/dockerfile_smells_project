FROM alpine:3.7

RUN  apk add --update --no-cache \
       lm_sensors \
       perl \
       bash
RUN  mkdir -p /home/node-exporter

COPY script.sh /home/

CMD ["/home/script.sh"]

