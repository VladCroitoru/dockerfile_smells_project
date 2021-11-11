FROM jboss/keycloak:1.9.5.Final

MAINTAINER Robert Brem <brem_robert@hotmail.com>

WORKDIR /opt/jboss/keycloak/standalone/configuration
ADD keycloak.jks .
ADD standalone.xml .
ADD keycloak-add-user.json .
