FROM verdel/alpine-base:latest
MAINTAINER Vadim Aleksandrov <valeksandrov@me.com>

RUN pip install --upgrade elasticsearch-curator

COPY rootfs /

RUN chmod 755 /sbin/*.sh

ENTRYPOINT ["/sbin/entrypoint.sh"]