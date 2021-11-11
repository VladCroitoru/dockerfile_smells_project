#Prometheus Config Store Dockerfile
FROM alpine
LABEL maintainer "Ed Marshall (ed@infinityworks.com)"

RUN mkdir -p /etc/prom-conf/

ADD prometheus.yml /etc/prom-conf/prometheus.yml

CMD ["/bin/sh"]
