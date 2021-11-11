FROM alpine:3.4

RUN apk add --update --no-cache docker

RUN mkdir -p /var/run/docker && \
  ln -s /etc/docker/ca.pem /var/run/docker/ca.pem && \
  ln -s /etc/docker/server-cert.pem /var/run/docker/cert.pem && \
  ln -s /etc/docker/server-key.pem /var/run/docker/key.pem

ADD start.sh /start.sh

VOLUME /etc/periodic/

CMD ["/start.sh"]
