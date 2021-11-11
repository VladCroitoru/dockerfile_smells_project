FROM        alpine:latest
MAINTAINER  Marrotte <marrotte@gmail.com>

WORKDIR /bin
COPY bin/nginx-sts-exporter /bin/
COPY docker-entrypoint.sh /bin/
RUN chmod +x /bin/nginx-sts-exporter

ENV NGINX_HOST "http://localhost"
ENV METRICS_ENDPOINT "/metrics"
ENV METRICS_ADDR ":9913"
ENV DEFAULT_METRICS_NS "nginx"

ENTRYPOINT ["docker-entrypoint.sh"]
