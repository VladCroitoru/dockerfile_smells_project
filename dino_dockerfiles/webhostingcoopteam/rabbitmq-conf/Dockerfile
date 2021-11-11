FROM alpine:latest

ADD https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-amd64 /confd
RUN chmod +x /confd

RUN ["apk", "update"]
RUN ["apk", "upgrade"]
RUN ["apk", "add", "bash"]

ADD ./conf.d /etc/confd/conf.d
ADD ./templates /etc/confd/templates
ADD ./run.sh /run.sh
ADD ./dockerentry.sh /dockerentry.sh

VOLUME /data/confd
VOLUME /opt/rancher/bin
VOLUME /etc/rabbitmq

RUN ["chmod", "+x", "/dockerentry.sh"]
ENTRYPOINT ["/dockerentry.sh"]
CMD ["--backend", "rancher", "--prefix", "/2015-07-25"]
