ARG WILDFLY_VERSION
FROM jboss/wildfly:$WILDFLY_VERSION

ARG POSTGRES_DRIVER_VERSION

COPY --chown=jboss:jboss setup-postgres-driver.cli /tmp/

RUN curl -o /tmp/postgresql-$POSTGRES_DRIVER_VERSION.jar https://jdbc.postgresql.org/download/postgresql-$POSTGRES_DRIVER_VERSION.jar && \
    printenv > env.properties && \
    $JBOSS_HOME/bin/jboss-cli.sh --file=/tmp/setup-postgres-driver.cli --properties=env.properties && \
    rm /tmp/setup-postgres-driver.cli && \
    rm /tmp/postgresql-$POSTGRES_DRIVER_VERSION.jar && \
    rm env.properties && \
    rm -rf $JBOSS_HOME/standalone/configuration/standalone_xml_history/current
#   ^^^ Fix for WFLYCTL0056: Could not rename /opt/jboss/wildfly/standalone/configuration/standalone_xml_history/current to ...

EXPOSE 8080 9990

CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
