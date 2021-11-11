FROM anapsix/alpine-java:8_jdk-dcevm_unlimited

# Configuration variables.
ENV BAMBOO_VERSION=6.7.1 \
    BAMBOO_HOME=/var/atlassian/application-data/bamboo \
    BAMBOO_INSTALL=/opt/atlassian/bamboo

RUN set -x \
    && apk --no-cache add libressl wget tar bash openssh tzdata maven git zip \
    && mkdir -p "${BAMBOO_HOME}" && mkdir -p "${BAMBOO_INSTALL}" \
    && wget -O "atlassian-bamboo-${BAMBOO_VERSION}.tar.gz" --no-verbose "http://www.atlassian.com/software/bamboo/downloads/binary/atlassian-bamboo-${BAMBOO_VERSION}.tar.gz" \
    && tar -xzvf "atlassian-bamboo-${BAMBOO_VERSION}.tar.gz" -C "${BAMBOO_INSTALL}" --strip-components=1 \
    && rm -rf atlassian-bamboo-${BAMBOO_VERSION}.tar.gz \
    && sed -i 's~bamboo.home=C:/bamboo/bamboo-home~bamboo.home=${BAMBOO_HOME}~g' ${BAMBOO_INSTALL}/atlassian-bamboo/WEB-INF/classes/bamboo-init.properties \
    && adduser -D -u 1000 bamboo \
    && chown -R bamboo:bamboo "${BAMBOO_HOME}" \
    && chown -R bamboo:bamboo "${BAMBOO_INSTALL}" \
    && mkdir /home/bamboo/.m2 \
    && chown -R bamboo:bamboo /home/bamboo/.m2 \
    && chmod -R 755 "${BAMBOO_HOME}" \
    && chmod -R 755 "${BAMBOO_INSTALL}" \
    && chmod -R 755 /home/bamboo/.m2 \
    && cp /usr/share/zoneinfo/Europe/London /etc/localtime \
    && sed -i 's~<Context path="" docBase="${catalina.home}/atlassian-bamboo~<Context path="/bamboo" docBase="${catalina.home}/atlassian-bamboo~g' ${BAMBOO_INSTALL}/conf/server.xml

# Expose default HTTP connector port.
EXPOSE 8085 16001 16002 7222

# Create the volumes and mount
VOLUME [ "${BAMBOO_HOME}" ]

WORKDIR ${BAMBOO_HOME}

USER bamboo
CMD ["sh", "-c", "${BAMBOO_INSTALL}/bin/catalina.sh run"]
