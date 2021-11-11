FROM alpine:3.6

MAINTAINER Nikola Petkanski <nikola@petkanski.com>

RUN adduser -u 1000 -D -g '' www-data
RUN apk --update add beanstalkd

EXPOSE 11300

ENTRYPOINT ["beanstalkd", "-p", "11300"]
