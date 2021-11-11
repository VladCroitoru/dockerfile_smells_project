FROM openjdk:8-jre-alpine
MAINTAINER Yun Zhi Lin <yun@yunspace.com>

# Set environment
ENV GOCD_VERSION=17.1.0 \
  GOCD_RELEASE=go-agent \
  GOCD_REVISION=4511 \
  GOCD_HOME=/opt/go-agent \
  PATH=$GOCD_HOME:$PATH \
  USER_HOME=/root
ENV GOCD_REPO=https://download.go.cd/binaries/${GOCD_VERSION}-${GOCD_REVISION}/generic \
  GOCD_RELEASE_ARCHIVE=${GOCD_RELEASE}-${GOCD_VERSION}-${GOCD_REVISION}.zip \
  SERVER_WORK_DIR=${GOCD_HOME}/work

ENV GLIBC 2.23-r3

RUN apk update && apk add --no-cache openssl ca-certificates && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC/glibc-$GLIBC.apk && \
    apk add --no-cache glibc-$GLIBC.apk && rm glibc-$GLIBC.apk && \
    ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ && \
    ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib

RUN apk add --no-cache --update py-pip && pip install docker-compose

# Install and configure gocd
RUN apk add --no-cache --update git curl bash openssh ca-certificates && rm -rf /var/cache/apk/* \
  && mkdir /opt /var/log/go-agent /var/run/go-agent \
  && cd /opt && curl -sSL ${GOCD_REPO}/${GOCD_RELEASE_ARCHIVE} -O && unzip ${GOCD_RELEASE_ARCHIVE} && rm ${GOCD_RELEASE_ARCHIVE} \
  && mv /opt/${GOCD_RELEASE}-${GOCD_VERSION} ${GOCD_HOME} \
  && chmod 774 ${GOCD_HOME}/*.sh \
  && mkdir -p ${GOCD_HOME}/work

# Add docker-entrypoint script
ADD docker-entrypoint.sh /usr/bin/docker-entrypoint.sh
RUN chmod +x /usr/bin/docker-entrypoint.sh

WORKDIR ${GOCD_HOME}

ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]
