FROM debian:wheezy
MAINTAINER Matt Bentley <mbentley@mbentley.net>

RUN (apt-get update &&\
  DEBIAN_FRONTEND=noninteractive apt-get install -y git live-build transmission-cli &&\
  mkdir /opt/live)

ADD run.sh /usr/local/bin/run

VOLUME ["/opt/live"]
ENTRYPOINT ["/usr/local/bin/run"]
CMD ["bash"]
