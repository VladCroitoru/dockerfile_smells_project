FROM turbulent/heap-base:2.0.3
MAINTAINER Benoit Beausejour <b@turbulent.ca>

ENV heap-memcached 2.0.1

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
  apt-get install -y memcached && \
  rm -rf /var/lib/apt/lists/*

ADD run.sh /run.sh

EXPOSE 11211

VOLUME ["/vol/logs"]
CMD ["/run.sh"]
