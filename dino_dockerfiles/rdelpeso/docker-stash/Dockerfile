FROM nathonfowlie/centos-jre:latest

# Setup useful environment variables
ENV STASH_HOME     /var/local/atlassian/stash
ENV STASH_INSTALL  /usr/local/atlassian/stash
ENV CONF_VERSION  3.4.5

# Install Atlassian Stash and helper tools and setup initial home
# directory structure.
RUN set -x \
    && yum install -y --quiet epel-release \
    && yum update -y --quiet \
    && yum install -y --quiet tomcat-native git-core xmlstarlet \
    && yum clean all --quiet \    
    && mkdir -p                "${STASH_HOME}/lib" \
    && mkdir -p -m 700         "${STASH_HOME}" \
    && chown daemon:daemon     "${STASH_HOME}" \
    && mkdir -p                "${STASH_INSTALL}" \
    && curl -Ls                "http://www.atlassian.com/software/stash/downloads/binary/atlassian-stash-${CONF_VERSION}.tar.gz" | tar -xz --directory "${STASH_INSTALL}" --strip-components=1 --no-same-owner \
    && chmod -R 700            "${STASH_INSTALL}/conf" \
    && chmod -R 700            "${STASH_INSTALL}/temp" \
    && chmod -R 700            "${STASH_INSTALL}/logs" \
    && chmod -R 700            "${STASH_INSTALL}/work" \
    && chown -R daemon:daemon  "${STASH_INSTALL}/conf" \
    && chown -R daemon:daemon  "${STASH_INSTALL}/temp" \
    && chown -R daemon:daemon  "${STASH_INSTALL}/logs" \
    && chown -R daemon:daemon  "${STASH_INSTALL}/work" \
    && ln --symbolic           "/usr/lib/x86_64-linux-gnu/libtcnative-1.so" "${STASH_INSTALL}/lib/native/libtcnative-1.so" \
    && sed --in-place         's/^# umask 0027$/umask 0027/g' "${STASH_INSTALL}/bin/setenv.sh" \
    && xmlstarlet              ed --inplace \
        --delete              "Server/Service/Engine/Host/@xmlValidation" \
        --delete              "Server/Service/Engine/Host/@xmlNamespaceAware" \
                              "${STASH_INSTALL}/conf/server.xml"

# Use the default unprivileged account. This could be considered bad practice
# on systems where multiple processes end up being executed by 'daemon' but
# here we only ever run one process anyway.
USER daemon:daemon

# Expose default HTTP connector port.
EXPOSE 7990 7999

# Set volume mount points for installation and home directory. Changes to the
# home directory needs to be persisted as well as parts of the installation
# directory due to eg. logs.
VOLUME ["/var/local/atlassian/stash"]

# Set the default working directory as the Stash home directory.
WORKDIR ${STASH_HOME}

# Run Atlassian STASH as a foreground process by default.
CMD ["/usr/local/atlassian/stash/bin/start-stash.sh", "-fg"]
