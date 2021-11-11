FROM dockage/alpine:3.6

LABEL maintainer="m.abdolirad@gmail.com" \
    org.label-schema.name="gearmand" \
    org.label-schema.vendor="Dockage" \
    org.label-schema.description="Gearman provides a generic application framework to farm out work to other machines or processes that are better suited to do the work." \
    org.label-schema.version="1.1.16" \
    org.label-schema.license="MIT"

ENV GEARMAND_VERSION=1.1.16 \
    GEARMAN_USER=gearman \
    GEARMAN_GROUP=gearman \
    DOCKAGE_ETC_DIR=/etc/dockage

ENV GEARMAN_HOME=/var/lib/${GEARMAN_USER}

ADD https://github.com/gearman/gearmand/releases/download/${GEARMAND_VERSION}/gearmand-${GEARMAND_VERSION}.tar.gz /
ADD ./assets ${DOCKAGE_ETC_DIR}

RUN apk update \
    && apk --no-cache add g++ libc-dev boost-dev gperf libevent-dev util-linux-dev hiredis-dev libressl-dev sqlite-dev libmemcached-dev \
    && ${DOCKAGE_ETC_DIR}/buildtime/install \
    && mv ${DOCKAGE_ETC_DIR}/sbin/* /sbin \
    && rm -rf /var/cache/apk/* ${DOCKAGE_ETC_DIR}/sbin ${DOCKAGE_ETC_DIR}/buildtime

EXPOSE 4730/tcp

ENTRYPOINT ["/sbin/entrypoint"]
CMD ["/sbin/su-exec", "${GEARMAN_USER}:${GEARMAN_GROUP}", "/usr/sbin/gearmand", "--log-file", "stderr"]
