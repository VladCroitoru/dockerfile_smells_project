FROM gradle:jdk8 as build
RUN mkdir -p /home/gradle/project
WORKDIR /home/gradle/project
COPY . /home/gradle/project
RUN gradle build --stacktrace

FROM sightseeker/wildfly-deployment-demo:11.0.0.Final
COPY deploy.cli /tmp
COPY --from=build /home/gradle/project/build/libs/webapp.war /tmp/
RUN /opt/jboss/wildfly/bin/jboss-cli.sh --file=/tmp/deploy.cli
RUN rm -rf /opt/jboss/wildfly/standalone/configuration/standalone_xml_history
