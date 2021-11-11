FROM ivonet/wildfly-admin:10.0.0.Final

MAINTAINER IvoNet <webmaster@ivonet.nl>

ENV KEYCLOAK_VERSION 2.3.0.Final

WORKDIR /opt/jboss/wildfly

RUN curl -L http://downloads.jboss.org/keycloak/$KEYCLOAK_VERSION/adapters/keycloak-oidc/keycloak-wildfly-adapter-dist-$KEYCLOAK_VERSION.tar.gz | tar zxv

WORKDIR /opt/jboss

# modifying standalone.xml to wire in the keycloak security provider
RUN sed -i -e 's/<extensions>/&\n        <extension module="org.keycloak.keycloak-adapter-subsystem"\/>/' $JBOSS_HOME/standalone/configuration/standalone.xml && \
    sed -i -e 's/<profile>/&\n        <subsystem xmlns="urn:jboss:domain:keycloak:1.1"\/>/' $JBOSS_HOME/standalone/configuration/standalone.xml && \
    sed -i -e 's/<security-domains>/&\n                <security-domain name="keycloak">\n                    <authentication>\n                        <login-module code="org.keycloak.adapters.jboss.KeycloakLoginModule" flag="required"\/>\n                    <\/authentication>\n                <\/security-domain>/' $JBOSS_HOME/standalone/configuration/standalone.xml

EXPOSE 8080 9990

