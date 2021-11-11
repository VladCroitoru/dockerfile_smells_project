FROM java:8
MAINTAINER Julien Fabre <ju.pryz@gmail.com>

ENV LEIN_VERSION=2.5.1
ENV LEIN_BIN=/usr/local/bin/lein
ENV LEIN_ROOT=1

RUN curl -o $LEIN_BIN \
  https://raw.githubusercontent.com/technomancy/leiningen/$LEIN_VERSION/bin/lein
RUN chmod a+x $LEIN_BIN

RUN lein
