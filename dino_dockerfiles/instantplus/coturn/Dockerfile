FROM debian:jessie
MAINTAINER Ivo von Putzer Reibegg <info@instant.plus>

ENV DEBIAN_FRONTEND noninteractive
ENV COTURN_VERSION 4.5.0.6

RUN ln -s -f /bin/true /usr/bin/chfn
RUN apt-get update
RUN apt-get install -y curl coturn procps --no-install-recommends

# RUN apt-get install -y sqlite libsqlite3-dev libevent-dev procps --no-install-recommends\
#  && curl -o /tmp/coturn.tar.gz -sL http://turnserver.open-sys.org/downloads/v${COTURN_VERSION}/turnserver-${COTURN_VERSION}.tar.gz\
#  && tar xvfz /tmp/coturn.tar.gz -C /tmp\
#  && cd /tmp/coturn\
#  && ./configure \
#  && make \
#  && make install

EXPOSE 3478 3478/udp
EXPOSE 3479 3479/udp
EXPOSE 5349 5349/udp
EXPOSE 5350 5350/udp

VOLUME /etc/letsencrypt
ENTRYPOINT ["/usr/bin/turnserver"]
