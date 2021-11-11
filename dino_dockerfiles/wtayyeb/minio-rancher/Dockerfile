FROM minio/minio:RELEASE.2018-07-13T00-09-07Z
MAINTAINER w.tayyeb <w.tayyeb@gmail.com>

# Application settings
ENV SCHEDULER_VOLUME="/opt/scheduler" \
    USER=minio \
    GROUP=minio \
    UID=10003 \
    GID=10003


# Install extra package
RUN apk --update add fping curl bash &&\
    rm -rf /var/cache/apk/*


# Install confd
ENV CONFD_VERSION="0.14.0" \
    CONFD_HOME="/opt/confd" \
    CONFD_PREFIX_KEY="/minio" \
    CONFD_BACKEND="env" \
    CONFD_INTERVAL="60" \
    CONFD_NODES=""

RUN mkdir -p "${CONFD_HOME}/etc/conf.d" "${CONFD_HOME}/etc/templates" "${CONFD_HOME}/log" "${CONFD_HOME}/bin" &&\
    curl -Lo "${CONFD_HOME}/bin/confd" "https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64" &&\
    chmod +x "${CONFD_HOME}/bin/confd"


# Install s6-overlay
ENV S6_VERSION="v1.19.1.1" \
    S6_BEHAVIOUR_IF_STAGE2_FAILS=2

RUN curl -sL https://github.com/just-containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz \
    | tar -zx -C /


# Install Glibc for minio
ENV GLIBC_VERSION="2.23-r4"

RUN apk add --update -t deps wget ca-certificates &&\
    cd /tmp &&\
    wget https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk &&\
    wget https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk &&\
    apk add --allow-untrusted glibc-${GLIBC_VERSION}.apk glibc-bin-${GLIBC_VERSION}.apk &&\
    /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib/ &&\
    echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf &&\
    apk del --purge deps &&\
    rm /tmp/* /var/cache/apk/*

# Install minio software
ENV APP_HOME="/opt/minio"

RUN mkdir -p ${APP_HOME}/log /data ${APP_HOME}/conf && \
    addgroup -g ${GID} ${GROUP} && \
    adduser -g "${USER} user" -D -h ${APP_HOME} -G ${GROUP} -s /bin/sh -u ${UID} ${USER} && \
    chown -R ${USER}:${GROUP} ${APP_HOME}

ADD root /

COPY ./docker-entrypoint.sh /usr/bin/
ENTRYPOINT []

CMD ["/init"]
