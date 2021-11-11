FROM tomcat:6-jre7
MAINTAINER Sean Herman <sjh293@cornell.edu>

ENV BUILD_DEPS='curl' \
    CONNECTORJ_MAJOR_VERSION='5' \
    CONNECTORJ_VERSION='5.1.38' \
    MYSQL_HOSTNAME='localhost' \
    ODK_PORT='8080' \
    ODK_PORT_SECURE='8443' \
    ODK_HOSTNAME='localhost' \
    ODK_ADMIN_USER='' \
    ODK_ADMIN_USERNAME='admin' \
    ODK_AUTH_REALM='ODK Aggregate'

RUN apt-get update \
    && apt-get install -y ${BUILD_DEPS} --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*; exit 0

RUN curl -OL https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${CONNECTORJ_VERSION}.tar.gz \
    && tar -xzf mysql-connector-java-${CONNECTORJ_VERSION}.tar.gz \
    && cp mysql-connector-java-$CONNECTORJ_VERSION/mysql-connector-java-${CONNECTORJ_VERSION}-bin.jar ${CATALINA_HOME}/lib/ \
    && rm -rf  mysql-connector-java-${CONNECTORJ_VERSION}/ mysql-connector-java-${CONNECTORJ_VERSION}.tar.gz

COPY run.sh /run.sh
COPY ODKAggregate.war /ODKAggregate.war
RUN chmod +x /run.sh

EXPOSE ${ODK_PORT}
ENTRYPOINT ["/run.sh"]
