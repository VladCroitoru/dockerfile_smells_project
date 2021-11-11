FROM blacklabelops/java:openjre8
MAINTAINER Steffen Bleul <sbl@blacklabelops.com>

ARG CRUCIBLE_VERSION=4.4.1
# permissions
ARG CONTAINER_UID=1000
ARG CONTAINER_GID=1000

ENV FISHEYE_INST=/var/atlassian/crucible \
    CRUCIBLE_INSTALL=/opt/crucible \
    CRUCIBLE_PROXY_NAME= \
    CRUCIBLE_PROXY_PORT= \
    CRUCIBLE_PROXY_SCHEME=

RUN export MYSQL_DRIVER_VERSION=5.1.38 && \
    export POSTGRESQL_DRIVER_VERSION=9.4.1207 && \
    export CONTAINER_USER=crucible &&  \
    export CONTAINER_GROUP=crucible &&  \
    addgroup -g $CONTAINER_GID $CONTAINER_GROUP &&  \
    adduser -u $CONTAINER_UID \
            -G $CONTAINER_GROUP \
            -h /home/$CONTAINER_USER \
            -s /bin/bash \
            -S $CONTAINER_USER &&  \
    apk add --update \
      git \
      mercurial \
      openssh \
      ca-certificates \
      unzip \
      curl \
      wget &&  \
    # Install xmlstarlet
    export XMLSTARLET_VERSION=1.6.1-r1              &&  \
    wget --directory-prefix=/tmp https://github.com/menski/alpine-pkg-xmlstarlet/releases/download/${XMLSTARLET_VERSION}/xmlstarlet-${XMLSTARLET_VERSION}.apk && \
    apk add --allow-untrusted /tmp/xmlstarlet-${XMLSTARLET_VERSION}.apk && \
    wget -O /tmp/crucible.zip https://www.atlassian.com/software/crucible/downloads/binary/crucible-${CRUCIBLE_VERSION}.zip && \
    unzip /tmp/crucible.zip -d /tmp && \
    mv /tmp/fecru-${CRUCIBLE_VERSION} /tmp/crucible && \
    mkdir -p ${FISHEYE_INST} && \
    mkdir -p /opt && \
    mv /tmp/crucible /opt/crucible && \
    # Install database drivers
    rm -f                                               \
      ${CRUCIBLE_INSTALL}/lib/mysql-connector-java*.jar &&  \
    wget -O /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz                                              \
      http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz && \
    tar xzf /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz                                              \
      -C /tmp && \
    cp /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-java-${MYSQL_DRIVER_VERSION}-bin.jar     \
      ${CRUCIBLE_INSTALL}/lib/mysql-connector-java-${MYSQL_DRIVER_VERSION}-bin.jar                                &&  \
    rm -f ${CRUCIBLE_INSTALL}/lib/postgresql-*.jar                                                                &&  \
    wget -O ${CRUCIBLE_INSTALL}/lib/postgresql-${POSTGRESQL_DRIVER_VERSION}.jar                                       \
      https://jdbc.postgresql.org/download/postgresql-${POSTGRESQL_DRIVER_VERSION}.jar && \
    # Adding letsencrypt-ca to truststore
    # Adding letsencrypt-ca to truststore
    export KEYSTORE=$JAVA_HOME/jre/lib/security/cacerts && \
    wget -P /tmp/ https://letsencrypt.org/certs/letsencryptauthorityx1.der && \
    wget -P /tmp/ https://letsencrypt.org/certs/letsencryptauthorityx2.der && \
    wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x1-cross-signed.der && \
    wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x2-cross-signed.der && \
    wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.der && \
    wget -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x4-cross-signed.der && \
    keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias isrgrootx1 -file /tmp/letsencryptauthorityx1.der && \
    keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias isrgrootx2 -file /tmp/letsencryptauthorityx2.der && \
    keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias letsencryptauthorityx1 -file /tmp/lets-encrypt-x1-cross-signed.der && \
    keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias letsencryptauthorityx2 -file /tmp/lets-encrypt-x2-cross-signed.der && \
    keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias letsencryptauthorityx3 -file /tmp/lets-encrypt-x3-cross-signed.der && \
    keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt -importcert -alias letsencryptauthorityx4 -file /tmp/lets-encrypt-x4-cross-signed.der && \
    # Install atlassian ssl tool
    wget -O /home/${CONTAINER_USER}/SSLPoke.class https://confluence.atlassian.com/kb/files/779355358/779355357/1/1441897666313/SSLPoke.class && \
    # Container user permissions
    chown -R crucible:crucible /home/${CONTAINER_USER} && \
    chown -R crucible:crucible ${FISHEYE_INST} && \
    chmod -R u=rwx,g=rwx,o=-rwx ${CRUCIBLE_INSTALL} && \
    chown -R crucible:crucible ${CRUCIBLE_INSTALL} && \
    # Install Tini Zombie Reaper And Signal Forwarder
    export TINI_VERSION=0.9.0 && \
    curl -fsSL https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-static -o /bin/tini && \
    chmod +x /bin/tini && \
    # Remove obsolete packages
    apk del \
      ca-certificates \
      unzip \
      curl \
      wget &&  \
    # Clean caches and tmps
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    rm -rf /var/log/*

USER crucible
WORKDIR /var/atlassian/crucible
VOLUME ["/var/atlassian/crucible"]
EXPOSE 8060
COPY imagescripts /home/crucible
ENTRYPOINT ["/bin/tini","--","/home/crucible/docker-entrypoint.sh"]
CMD ["crucible"]
