FROM java:8

# Setup useful environment variables
ENV CONFLUENCE_HOME     /var/atlassian/confluence
ENV CONFLUENCE_INSTALL  /opt/atlassian/confluence
ENV CONFLUENCE_VERSION  5.10.8

# Install Atlassian Confluence and hepler tools and setup initial home
# directory structure.
RUN set -x \
    && apt-get update --quiet \
    && apt-get install --quiet --yes --no-install-recommends libtcnative-1 xmlstarlet postgresql-client \
    && apt-get clean \
    && mkdir -p                "${CONFLUENCE_HOME}" \
    && chmod -R 700            "${CONFLUENCE_HOME}" \
    && chown daemon:daemon     "${CONFLUENCE_HOME}" \
    && mkdir -p                "${CONFLUENCE_INSTALL}/conf" \
    && curl -Ls                "https://www.atlassian.com/software/confluence/downloads/binary/atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz" | tar -xz --directory "${CONFLUENCE_INSTALL}" --strip-components=1 --no-same-owner \
    && curl -Ls                "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.38.tar.gz" | tar -xz --directory "${CONFLUENCE_INSTALL}/confluence/WEB-INF/lib" --strip-components=1 --no-same-owner "mysql-connector-java-5.1.38/mysql-connector-java-5.1.38-bin.jar" \
    && chmod -R 700            "${CONFLUENCE_INSTALL}/conf" \
    && chmod -R 700            "${CONFLUENCE_INSTALL}/temp" \
    && chmod -R 700            "${CONFLUENCE_INSTALL}/logs" \
    && chmod -R 700            "${CONFLUENCE_INSTALL}/work" \
    && chown -R daemon:daemon  "${CONFLUENCE_INSTALL}/conf" \
    && chown -R daemon:daemon  "${CONFLUENCE_INSTALL}/temp" \
    && chown -R daemon:daemon  "${CONFLUENCE_INSTALL}/logs" \
    && chown -R daemon:daemon  "${CONFLUENCE_INSTALL}/work" \
    && echo -e                 "\nconfluence.home=$CONFLUENCE_HOME" >> "${CONFLUENCE_INSTALL}/confluence/WEB-INF/classes/confluence-init.properties" \
    && xmlstarlet              ed --inplace \
        --delete               "Server/@debug" \
        --delete               "Server/Service/Connector/@debug" \
        --delete               "Server/Service/Connector/@useURIValidationHack" \
        --delete               "Server/Service/Connector/@minProcessors" \
        --delete               "Server/Service/Connector/@maxProcessors" \
        --delete               "Server/Service/Engine/@debug" \
        --delete               "Server/Service/Engine/Host/@debug" \
        --delete               "Server/Service/Engine/Host/Context/@debug" \
                               "${CONFLUENCE_INSTALL}/conf/server.xml" \
    && touch -d "@0"           "${CONFLUENCE_INSTALL}/conf/server.xml"

#COPY "resources/confluence.cfg.xml.template" "${CONFLUENCE_HOME}/"
#RUN chown daemon:daemon "${CONFLUENCE_HOME}/confluence.cfg.xml.template"

COPY "resources/docker-entrypoint.sh" "/"
RUN chmod +x /docker-entrypoint.sh

# Use the default unprivileged account. This could be considered bad practice
# on systems where multiple processes end up being executed by 'daemon' but
# here we only ever run one process anyway.
USER daemon:daemon

# Expose default HTTP connector port.
EXPOSE 8090

# Set volume mount points for installation and home directory. Changes to the
# home directory needs to be persisted as well as parts of the installation
# directory due to eg. logs.
#VOLUME ["/var/atlassian/confluence", "/opt/atlassian/confluence/logs"]

# Set the default working directory as the Confluence home directory.
WORKDIR /var/atlassian/confluence

ENTRYPOINT ["/docker-entrypoint.sh"]

# Run Atlassian Confluence as a foreground process by default.
CMD ["/opt/atlassian/confluence/bin/catalina.sh", "run"]