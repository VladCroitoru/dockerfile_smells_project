FROM gliderlabs/alpine:3.4
MAINTAINER Vicko Vitasovic "vickovitasovic@gmail.com"

RUN apk --no-cache add --update \
    bash \
    python-dev \
    py-pip \
    py-mysqldb \
  && pip install sandman2 \
  && rm -rf /var/cache/apk/*

ADD entrypoint /app/

EXPOSE 5000
ENTRYPOINT ["/app/entrypoint"]
