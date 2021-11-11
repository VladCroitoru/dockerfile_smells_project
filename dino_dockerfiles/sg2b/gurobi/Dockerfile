FROM python:2.7-alpine
MAINTAINER Julien Deruere <deruere.julien@gmail.com>

ENV GUROBI_INSTALL /opt/gurobi
ENV GUROBI_HOME $GUROBI_INSTALL/linux64
ENV PATH $PATH:$GUROBI_HOME/bin
ENV LD_LIBRARY_PATH $GUROBI_HOME/lib

ARG GUROBI_MAJOR_VERSION=6.5
ARG GUROBI_VERSION=6.5.2
ARG user=gurobi
ARG group=gurobi
ARG uid=1000
ARG gid=1000

RUN apk upgrade --update && \
    apk add --update        \
      bash                  \
      ca-certificates       \
      gzip                  \
      curl                  \
      wget               && \
    # Add user
    addgroup -g ${gid} ${group}                                           && \
    adduser -h /home/gurobi -u ${uid} -G ${group} -s /bin/bash -D ${user} && \
    # Install latest glibc
    export GLIBC_VERSION=2.23-r3                                                                                                  && \
    apk --no-cache add ca-certificates                                                                                            && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub && \
    wget -P /tmp https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk       && \
    wget -P /tmp https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk   && \
    wget -P /tmp https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-i18n-${GLIBC_VERSION}.apk  && \
    apk add /tmp/glibc-${GLIBC_VERSION}.apk /tmp/glibc-bin-${GLIBC_VERSION}.apk /tmp/glibc-i18n-${GLIBC_VERSION}.apk              && \
    /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8                                                                 && \
    # Install gurobi
    mkdir -p ${GUROBI_INSTALL}                                                                                      && \
    wget -P /home/gurobi/ http://packages.gurobi.com/${GUROBI_MAJOR_VERSION}/gurobi${GUROBI_VERSION}_linux64.tar.gz && \
    tar xvfz /home/gurobi/gurobi${GUROBI_VERSION}_linux64.tar.gz                                                    && \
    mv /gurobi652/linux64/ ${GUROBI_INSTALL}                                                                        && \                                                                        \
    # Clean up
    rm -rf ${GUROBI_HOME}/docs                             && \
    rm -rf ${GUROBI_HOME}/examples                         && \
    rm -rf ${GUROBI_HOME}/src                              && \
    rm -rf /var/cache/apk/*                                && \
    rm -rf /tmp/*                                          && \
    rm -rf /var/log/*                                      && \
    rm -rf /gurobi652                                      && \
    rm /home/gurobi/gurobi${GUROBI_VERSION}_linux64.tar.gz && \
    # Remove obsolete packages
    apk del             \
      ca-certificates   \
      gzip              \
      curl              \
      wget

COPY scripts/docker-entrypoint.sh ${GUROBI_HOME}/bin

# Set permissions
RUN chown -R gurobi ${GUROBI_HOME} && \
    chmod 755 ${GUROBI_HOME}/bin/docker-entrypoint.sh

USER gurobi

WORKDIR /usr/src/gurobi/scripts

VOLUME /usr/src/gurobi/scripts
VOLUME /home/gurobi

ENTRYPOINT ["docker-entrypoint.sh"]