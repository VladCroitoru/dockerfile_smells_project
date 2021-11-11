FROM jboss/keycloak-openshift

ADD application.keystore /opt/jboss/keycloak/standalone/configuration/

ENTRYPOINT [ "/opt/jboss/tools/docker-entrypoint.sh" ]

CMD ["-b", "0.0.0.0"]
