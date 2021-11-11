FROM alpine:3.6

LABEL maintainer="Juliano Petronetto <juliano@petronetto.com.br>"
LABEL org.label-schema.name="Beanstalkd Alpine" \
      org.label-schema.description="Beanstalkd in Alpine Linux" \
      org.label-schema.url="https://hub.docker.com/r/petronetto/beanstalkd-alpine/" \
      org.label-schema.vcs-url="https://github.com/petronetto/beanstalkd-alpine" \
      org.label-schema.vendor="Petroneto DevTech" \
      org.label-schema.version="1.0" \
      org.label-schema.schema-version="1.0"

ENV VERSION_BEANSTALKD="1.10"

RUN addgroup -S beanstalkd && adduser -S -G beanstalkd beanstalkd
RUN apk add --no-cache 'su-exec>=0.2'

RUN apk --update add beanstalkd && \
    rm -rf /tmp/* && \
    rm -rf /var/cache/apk/*
  
RUN mkdir /data && chown beanstalkd:beanstalkd /data

VOLUME ["/data"]

EXPOSE 11300

ENTRYPOINT ["beanstalkd", "-p", "11300", "-u", "beanstalkd"]
CMD ["-b", "/data"]
