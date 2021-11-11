FROM adoptopenjdk/openjdk8:alpine

ENV CONFLUENCE_VERSION=6.13.8 \
    CONFLUENCE_HOME=/var/atlassian/application-data/confluence \
    CONFLUENCE_INSTALL=/opt/atlassian/confluence \
    MYSQL_VERSION=5.1.38 \
    POSTGRES_VERSION=9.4.1212
    
RUN set -x \
    && apk add --no-cache wget libressl tar tzdata bash fontconfig ttf-dejavu \
    && mkdir -p "${CONFLUENCE_HOME}" \
    && mkdir -p "${CONFLUENCE_INSTALL}/conf" \
    && wget -O "atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz" --no-verbose "https://www.atlassian.com/software/confluence/downloads/binary/atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz" \
    && wget -O "mysql-connector-java-${MYSQL_VERSION}.tar.gz" --no-verbose "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_VERSION}.tar.gz" \
    && wget -O "postgresql-${POSTGRES_VERSION}.jar" "https://jdbc.postgresql.org/download/postgresql-${POSTGRES_VERSION}.jar" \
    && tar -xzvf "atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz" -C "${CONFLUENCE_INSTALL}" --strip-components=1 \
    && tar -xzvf "mysql-connector-java-${MYSQL_VERSION}.tar.gz" -C "${CONFLUENCE_INSTALL}/confluence/WEB-INF/lib" --strip-components=1 \
    && mv "postgresql-${POSTGRES_VERSION}.jar" "${CONFLUENCE_INSTALL}/confluence/WEB-INF/lib/postgresql-${POSTGRES_VERSION}.jar" \
    && echo -e "\nconfluence.home=${CONFLUENCE_HOME}" >> "${CONFLUENCE_INSTALL}/confluence/WEB-INF/classes/confluence-init.properties" \
    && rm -rf "atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz" \
    && rm -rf "mysql-connector-java-${MYSQL_VERSION}.tar.gz" \
    && adduser -D -u 1000 confluence \
    && chown -R confluence "${CONFLUENCE_HOME}" \
    && chown -R confluence "${CONFLUENCE_INSTALL}/conf" \
    && chown -R confluence "${CONFLUENCE_INSTALL}/logs" \
    && chown -R confluence "${CONFLUENCE_INSTALL}/temp" \
    && chown -R confluence "${CONFLUENCE_INSTALL}/work" \
    && chmod -R 700 "${CONFLUENCE_HOME}" \
    && chmod -R 700 "${CONFLUENCE_INSTALL}/conf" \
    && chmod -R 700 "${CONFLUENCE_INSTALL}/logs" \
    && chmod -R 700 "${CONFLUENCE_INSTALL}/temp" \
    && chmod -R 700 "${CONFLUENCE_INSTALL}/work" \
    && cp /usr/share/zoneinfo/Europe/London /etc/localtime

# Expose default HTTP connector ports 
EXPOSE 8090 8091

VOLUME ["${CONFLUENCE_HOME}"]

WORKDIR ${CONFLUENCE_INSTALL}

USER confluence
CMD ["sh", "-c", "${CONFLUENCE_INSTALL}/bin/catalina.sh run"]

