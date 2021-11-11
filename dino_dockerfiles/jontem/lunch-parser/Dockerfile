FROM clojure:boot-2.7.1-alpine
MAINTAINER jontem
ENV BOOT_AS_ROOT=yes

WORKDIR /tmp
RUN mkdir /tmp/cache

ADD src /tmp/src
ADD build.boot /tmp/

RUN boot