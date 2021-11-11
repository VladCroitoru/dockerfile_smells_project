FROM jboss/wildfly:20.0.1.Final

LABEL description="Imixs-Admin"
LABEL maintainer="ralph.soika@imixs.com"

# Deploy artefact
ADD ./src/docker/apps/imixs-admin.war /opt/jboss/wildfly/standalone/deployments/
