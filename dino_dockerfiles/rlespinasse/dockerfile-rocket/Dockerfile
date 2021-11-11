# CoreOS Rocket
#
# VERSION               0.1.1

FROM ubuntu
MAINTAINER Romain Lespinasse <romain.lespinasse@gmail.com>

ADD https://github.com/coreos/rocket/releases/download/v0.1.1/rocket-v0.1.1.tar.gz /
RUN tar xzvf rocket-v0.1.1.tar.gz \
      && rm rocket-v0.1.1.tar.gz \
      && ln -s /rocket-v0.1.1/rkt /usr/bin/rkt \
      && ln -s /rocket-v0.1.1/actool /usr/bin/actool
