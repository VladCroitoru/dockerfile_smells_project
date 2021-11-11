FROM ubuntu:14.04

MAINTAINER Ron Kurr <kurr@kurron.org>

RUN apt-get update && \
    apt-get install -y nfs-common && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*


ENV OPTIONS nolock
ENV SERVER 192.168.1.234
ENV MOUNT /media

VOLUME /media

ADD mount.sh /mount.sh

ENTRYPOINT ["/mount.sh"]
