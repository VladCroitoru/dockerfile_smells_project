FROM alpine:3.3

ENV version="1.10"

RUN apk --update add --virtual build-dependencies gcc make musl-dev curl bash \
  && curl -sL https://github.com/kr/beanstalkd/archive/v$version.tar.gz | tar xvz -C /tmp \
  && cd /tmp/beanstalkd-$version \
  && sed -i "s|#include <sys/fcntl.h>|#include <fcntl.h>|g" sd-daemon.c \
  && make \
  && cp beanstalkd /usr/bin \
  && apk del build-dependencies \
  && rm -rf /tmp/* \
  && rm -rf /var/cache/apk/* 

EXPOSE 11300
CMD ["/usr/bin/beanstalkd", "-p", "11300", "-l", "0.0.0.0", "-z", "65535", "-u", "nobody"]
