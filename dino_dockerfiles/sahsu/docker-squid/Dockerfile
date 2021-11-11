FROM ubuntu
MAINTAINER sahsu.mobi@gmail.com

ENV MAX_OBJECT_SIZE=512 \
    CACHE_MEM=32 \
    SQUID_CACHE_DIR=/var/spool/squid3 \
    SQUID_LOG_DIR=/var/log/squid3 \
    SQUID_USER=proxy


RUN apt-get update -y && apt-get install -y squid && apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY squid.conf /etc/squid3/squid.conf

RUN echo "maximum_object_size ${MAX_OBJECT_SIZE} MB" >> /etc/squid3/squid.conf
RUN echo "cache_mem ${CACHE_MEM} MB" >> /etc/squid3/squid.conf

COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

EXPOSE 3128/tcp
VOLUME ["${SQUID_CACHE_DIR}"]
ENTRYPOINT ["/sbin/entrypoint.sh"]

