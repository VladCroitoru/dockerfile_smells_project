FROM anapsix/alpine-java:8_jdk-dcevm_unlimited

# Configuration variables.
ENV FISHEYE_VERSION=4.6.0 \
    FISHEYE_INST=/opt/atlassian/fisheye \
    MYSQL_VERSION=5.1.38

RUN set -x \
    && apk add --no-cache libressl wget tar bash unzip git \
    && mkdir -p "${FISHEYE_INST}" \
    && wget -O "atlassian-fisheye-${FISHEYE_VERSION}.zip" --no-verbose "https://www.atlassian.com/software/fisheye/downloads/binary/fisheye-${FISHEYE_VERSION}.zip" \
    && wget -O "mysql-connector-java-${MYSQL_VERSION}.tar.gz" --no-verbose "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_VERSION}.tar.gz" \
    && unzip -o atlassian-fisheye-${FISHEYE_VERSION}.zip -d /tmp \
    && yes | cp -rf /tmp/fecru-${FISHEYE_VERSION}/* ${FISHEYE_INST}/. \
    && tar -xzvf "mysql-connector-java-${MYSQL_VERSION}.tar.gz" -C "${FISHEYE_INST}/lib" --strip-components=1 \
    && rm -rf /tmp/fecru-${FISHEYE_VERSION}/*.* \
    && rm -rf "mysql-connector-java-${MYSQL_VERSION}.tar.gz" \
    && rm -rf "atlassian-fisheye-${FISHEYE_VERSION}.zip" \
    && adduser -D -u 1000 fisheye \
    && chown -R fisheye "${FISHEYE_INST}" \
    && chmod -R 700 "${FISHEYE_INST}"

# Expose default HTTP connector port.
EXPOSE 8060

VOLUME [ "${FISHEYE_INST}" ]

WORKDIR ${FISHEYE_INST}

USER fisheye

ENTRYPOINT ["bin/fisheyectl.sh", "run"]
