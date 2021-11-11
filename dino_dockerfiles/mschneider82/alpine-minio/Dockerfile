FROM alpine:3.6
MAINTAINER Matthias Schneider <ms@wck.biz>

# Application settings
ENV CONFD_PREFIX_KEY="/minio" \
    CONFD_BACKEND="env" \
    CONFD_INTERVAL="60" \
    CONFD_NODES="" \
    S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \
    APP_HOME="/opt/minio" \
    APP_VERSION="RELEASE.2018-11-15T01-26-07Z" \
    SCHEDULER_VOLUME="/opt/scheduler" \
    USER=minio \
    GROUP=minio \
    UID=10003 \
    GID=10003 \
    CONTAINER_NAME="alpine-minio" \
    CONTAINER_AUHTOR="Matthias Schneider <ms@wck.biz>" \
    CONTAINER_SUPPORT="https://github.com/mschneider82/alpine-minio/issues" \
    APP_WEB="https://minio.io/" \
    TLS_FQDN=""

# Install extra package
RUN apk --update add fping curl bash &&\
    rm -rf /var/cache/apk/*

# Install confd
ENV CONFD_VERSION="0.14.0" \
    CONFD_HOME="/opt/confd"
RUN mkdir -p "${CONFD_HOME}/etc/conf.d" "${CONFD_HOME}/etc/templates" "${CONFD_HOME}/log" "${CONFD_HOME}/bin" &&\
    curl -Lo "${CONFD_HOME}/bin/confd" "https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64" &&\
    chmod +x "${CONFD_HOME}/bin/confd"

# Install s6-overlay
RUN curl -sL https://github.com/just-containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz \
    | tar -zx -C /


# Install Glibc for minio
ENV GLIBC_VERSION="2.23-r1"
RUN \
    apk add --update -t deps wget ca-certificates &&\
    cd /tmp &&\
    wget https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk &&\
    wget https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk &&\
    apk add --allow-untrusted glibc-${GLIBC_VERSION}.apk glibc-bin-${GLIBC_VERSION}.apk &&\
    /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib/ &&\
    echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf &&\
    apk del --purge deps &&\
    rm /tmp/* /var/cache/apk/*

# Install minio software
RUN \
    mkdir -p ${APP_HOME}/log /data ${APP_HOME}/bin ${APP_HOME}/conf && \
    curl -f https://dl.minio.io/server/minio/release/linux-amd64/minio.${APP_VERSION} -o ${APP_HOME}/bin/minio && \
    addgroup -g ${GID} ${GROUP} && \
    adduser -g "${USER} user" -D -h ${APP_HOME} -G ${GROUP} -s /bin/sh -u ${UID} ${USER}

# Install generate_cert
RUN curl -fgL -o /usr/bin/generate_cert https://github.com/SvenDowideit/generate_cert/releases/download/0.3/generate_cert-0.3-linux-amd64 && \
    chmod +x /usr/bin/generate_cert


RUN mkdir -p ${APP_HOME}/.minio/certs

ADD root /
RUN chmod +x ${APP_HOME}/bin/* &&\
    chown -R ${USER}:${GROUP} ${APP_HOME}

VOLUME ["/data"]
EXPOSE 9000
CMD ["/init"]
