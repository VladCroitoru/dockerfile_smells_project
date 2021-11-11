FROM jboss/wildfly
MAINTAINER Marcin Wolański "wolanskim@gmail.com"
ENV REFRESHED_AT 2015-03-18

ENV DROOLS_WORKBENCH_VERSION 6.2.0.Final

RUN curl http://central.maven.org/maven2/org/kie/kie-drools-wb-distribution-wars/$DROOLS_WORKBENCH_VERSION/kie-drools-wb-distribution-wars-$DROOLS_WORKBENCH_VERSION-wildfly8.war > /opt/jboss/wildfly/standalone/deployments/drools-workbench.war
RUN bash /opt/jboss/wildfly/bin/add-user.sh --silent=true -a admin welcome1
RUN sed -i "\$aadmin=admin" /opt/jboss/wildfly/standalone/configuration/application-roles.properties
