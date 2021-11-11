FROM debian:stretch-slim

# this fork is maintained by kleberbaum
MAINTAINER Florian Kleber <kleberbaum@erebos.xyz>

ARG TINI_VERSION="v0.16.1"

WORKDIR /opt

ADD assets/generate_ca_and_server_certs.sh /opt/scripts/generate_ca_and_server_certs.sh
ADD assets/vars.template /opt/scripts/
ADD opt/ /opt/openvpn-gui/
ADD assets/app.conf /opt/openvpn-gui/conf/app.conf

# update, install and cleaning
RUN echo "## Installing base ##" && \
    apt-get update && \
    apt-get install -y \
            curl \
            gnupg \
            easy-rsa \
    && chmod 755 /usr/share/easy-rsa/* \
    \
    echo "## Installing tini ##" && \
    && set -x \
    && export TINI_HOME="/sbin/" \
    && curl -fSL "https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini" -o "${TINI_HOME}/tini" \
    && curl -fSL "https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini.asc" -o "${TINI_HOME}/tini.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 6380DC428747F6C393FEACA59A84159D7001A4E5 \
    && gpg --batch --verify "${TINI_HOME}/tini.asc" "${TINI_HOME}/tini" \
    && rm -r "$GNUPGHOME" "${TINI_HOME}/tini.asc" \
    && chmod +x "${TINI_HOME}/tini" \
    && "${TINI_HOME}/tini" -h \
    \
    && apt-get clean \
    && rm -Rf /var/lib/apt/lists/* 2>/dev/null

EXPOSE 8080/tcp

# place init
ADD assets/start.sh /run.sh
RUN chmod +x /run.sh

# I personally like to start my containers with tini
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["run.sh"]
