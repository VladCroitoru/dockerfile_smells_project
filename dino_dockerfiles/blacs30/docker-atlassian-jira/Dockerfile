##############################################################################
# Dockerfile to build Atlassian Jira container images
# Based on frolvlad/alpine-oraclejdk8:cleaned
##############################################################################

FROM frolvlad/alpine-oraclejdk8:cleaned
MAINTAINER Blacs30 <gitlab@lisowski-development.com>

# permissions
ARG CONTAINER_UID=1000
ARG CONTAINER_GID=1000

ARG VERSION=7.13.0

# Setup useful environment variables
ENV JIRA_INST=/opt/jira \
  JIRA_HOME=/var/atlassian/jira \
  SYSTEM_USER=jira \
  SYSTEM_GROUP=jira \
  SYSTEM_HOME=/home/jira \
  MYSQL_DRIVER_VERSION=5.1.38 \
  POSTGRESQL_DRIVER_VERSION=9.4.1212

# Install Atlassian JIRA and helper tools and setup initial home
# directory structure.
RUN set -x \
  && apk update \
  && apk add \
  bash \
  tar \
  xmlstarlet \
  wget \
  ca-certificates \
  --update-cache \
  --allow-untrusted \
  --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
  --repository http://dl-cdn.alpinelinux.org/alpine/edge/community \
  && update-ca-certificates    \
  && mkdir -p ${JIRA_INST} \
  && mkdir -p ${JIRA_HOME} \
  && mkdir -p "${JIRA_HOME}/caches/indexes" \
  && mkdir -p "${JIRA_INST}/conf/Catalina" \
  && mkdir -p ${SYSTEM_HOME} \
  && addgroup -S ${SYSTEM_GROUP} \
  && adduser -S -D -G ${SYSTEM_GROUP} -h ${SYSTEM_HOME} -s /bin/sh ${SYSTEM_USER} \
  && chown -R ${SYSTEM_USER}:${SYSTEM_GROUP} ${SYSTEM_HOME} \
  && wget -O /tmp/atlassian-jira-${VERSION}.tar.gz https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-${VERSION}.tar.gz \
  && tar xfz /tmp/atlassian-jira-${VERSION}.tar.gz --strip-components=1 -C ${JIRA_INST} \
  && rm /tmp/atlassian-jira-${VERSION}.tar.gz \
  && chown -R ${SYSTEM_USER}:${SYSTEM_GROUP} ${JIRA_INST} \
  && touch -d "@0" "${JIRA_INST}/conf/server.xml" \
  && touch -d "@0" "${JIRA_INST}/bin/setenv.sh" \
  && touch -d "@0" "${JIRA_INST}/atlassian-jira/WEB-INF/classes/jira-application.properties" \
  && rm -f ${JIRA_INST}/lib/mysql-connector-java*.jar \
  && wget -O /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz \
  && tar xzf /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}.tar.gz -C /tmp \
  && cp /tmp/mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-java-${MYSQL_DRIVER_VERSION}-bin.jar ${JIRA_INST}/lib/mysql-connector-java-${MYSQL_DRIVER_VERSION}-bin.jar \
  && rm -f ${JIRA_INST}/lib/postgresql-*.jar \
  && wget -O ${JIRA_INST}/lib/postgresql-${POSTGRESQL_DRIVER_VERSION}.jar https://jdbc.postgresql.org/download/postgresql-${POSTGRESQL_DRIVER_VERSION}.jar \
  && rm -rf /var/cache/apk/*                   \
  && rm -rf /tmp/*                                   \
  && rm -rf /var/log/*

ADD files/service /usr/local/bin/service
ADD files/entrypoint /usr/local/bin/entrypoint

EXPOSE 8080

# Set volume mount points for installation and home directory. Changes to the
# home directory needs to be persisted as well as parts of the installation
# directory due to eg. logs.
VOLUME [ "${JIRA_HOME}", "/opt/jira/logs", "/var/atlassian/jira/export"]

ENTRYPOINT ["/usr/local/bin/entrypoint"]

CMD ["/usr/local/bin/service"]
