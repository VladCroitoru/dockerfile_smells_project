FROM openjdk:8-jre-alpine

RUN apk --no-cache add bash

RUN wget -qO- http://apache.mirrors.lucidnetworks.net/zeppelin/zeppelin-0.8.0/zeppelin-0.8.0-bin-all.tgz | tar zxv -C /
RUN ln -nsf /zeppelin-* /zeppelin

ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT /entrypoint.sh

