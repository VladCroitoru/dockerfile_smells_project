FROM jboss/base-jdk:8

ENV KEYCLOAK_VERSION 3.1.0.Final
# Enables signals getting passed from startup script to JVM
# ensuring clean shutdown when container is stopped.
ENV LAUNCH_JBOSS_IN_BACKGROUND 1
ENV PROXY_ADDRESS_FORWARDING false
USER root

RUN yum install -y epel-release && yum install -y jq && yum clean all

USER jboss

RUN cd /opt/jboss/ && curl -L https://downloads.jboss.org/keycloak/$KEYCLOAK_VERSION/keycloak-$KEYCLOAK_VERSION.tar.gz | tar zx && mv /opt/jboss/keycloak-$KEYCLOAK_VERSION /opt/jboss/keycloak

COPY docker-entrypoint.sh /opt/jboss/

USER root
#Ensure docker-entrypoint.sh is executable
RUN chmod 755 /opt/jboss/docker-entrypoint.sh
USER jboss

ENV JBOSS_HOME /opt/jboss/keycloak

#Enable MySQL and HTTPS/SSL
COPY clicktoshare.jks $JBOSS_HOME/standalone/configuration
COPY standalone.xml $JBOSS_HOME/standalone/configuration
RUN mkdir -p $JBOSS_HOME/modules/system/layers/base/com/mysql/jdbc/main; cd $JBOSS_HOME/modules/system/layers/base/com/mysql/jdbc/main && curl -O http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.18/mysql-connector-java-5.1.18.jar
COPY module.xml $JBOSS_HOME/modules/system/layers/base/com/mysql/jdbc/main/

#Enabling Proxy address forwarding so we can correctly handle SSL termination in front ends
#such as an OpenShift Router or Apache Proxy
RUN sed -i -e 's/<http-listener /& proxy-address-forwarding="${env.PROXY_ADDRESS_FORWARDING}" /' $JBOSS_HOME/standalone/configuration/standalone.xml

#Expose HTTP Port
EXPOSE 8080

#Expose HTTPS Port
EXPOSE 8443

ENTRYPOINT [ "/opt/jboss/docker-entrypoint.sh" ]

CMD ["-b", "0.0.0.0"]

USER root
#Give correct permissions when used in an OpenShift environment.
RUN chown -R jboss:0 $JBOSS_HOME/standalone && \
    chmod -R g+rw $JBOSS_HOME/standalone
USER jboss
