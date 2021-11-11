FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN addgroup no-root && \
    adduser \
      --system \
      --ingroup no-root \
      --disabled-login \
      no-root

RUN mkdir /var/nfs-test

ADD nfs-test.sh /
RUN chmod +x /nfs-test.sh

USER no-root
VOLUME ["/var/nfs-test"]
ENTRYPOINT ["/nfs-test.sh"]
