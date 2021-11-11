FROM ubuntu:xenial
RUN apt-get update && apt-get install -y apt-mirror
VOLUME /var/spool/apt-mirror/
CMD /usr/bin/apt-mirror
