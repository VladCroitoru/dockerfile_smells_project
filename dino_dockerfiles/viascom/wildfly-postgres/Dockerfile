FROM viascom/base-wildfly:10.1.0

USER wildfly

ENV POSTGRESQL_JDBC_DRIVER_VERSION 42.2.1

RUN wget -q "https://jdbc.postgresql.org/download/postgresql-${POSTGRESQL_JDBC_DRIVER_VERSION}.jar" -O ${WILDFLY_HOME}/postgresql-${POSTGRESQL_JDBC_DRIVER_VERSION}.jar

ADD datasource.cli ${WILDFLY_HOME}/datasource.cli
RUN sed -i -e s/POSTGRESQL-JDBC-DRIVER-VERSION/${POSTGRESQL_JDBC_DRIVER_VERSION}/g ${WILDFLY_HOME}/datasource.cli

RUN ${WILDFLY_HOME}/bin/jboss-cli.sh --file=${WILDFLY_HOME}/datasource.cli
RUN rm -rf ${WILDFLY_HOME}/standalone/configuration/standalone_xml_history

ENTRYPOINT ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
