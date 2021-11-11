FROM alpine

RUN apk update \
    && apk --no-cache --progress add beanstalkd

VOLUME ["/data"]

EXPOSE 11300

CMD ["/usr/bin/beanstalkd", "-f", "60000", "-b", "/data"]
