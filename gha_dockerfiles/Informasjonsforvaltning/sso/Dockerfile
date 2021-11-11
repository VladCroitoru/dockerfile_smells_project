FROM maven:3.6.3-ibmjava-8-alpine AS MAVEN_BUILD_ENVIRONMENT

# use maven environment to build java modules

RUN mkdir /tmp/rest-user-mapper
RUN mkdir /tmp/whitelisted-email-validator

COPY modules/rest-user-mapper/pom.xml /tmp/rest-user-mapper/
COPY modules/rest-user-mapper/src /tmp/rest-user-mapper/src/

WORKDIR /tmp/rest-user-mapper/
RUN mvn clean package --no-transfer-progress

COPY modules/whitelisted-email-validator/pom.xml /tmp/whitelisted-email-validator/
COPY modules/whitelisted-email-validator/src /tmp/whitelisted-email-validator/src/

WORKDIR /tmp/whitelisted-email-validator
RUN mvn clean package --no-transfer-progress

###################################

FROM jboss/keycloak:6.0.1

ENV DB_VENDOR h2

# copy deployment modules from maven environment
# deployments are compiled SPI implementation modules. E.g. Federated rest user storage module.
COPY --from=MAVEN_BUILD_ENVIRONMENT /tmp/rest-user-mapper/target/rest-user-mapper.jar /opt/jboss/keycloak/standalone/deployments/rest-user-mapper.jar
COPY --from=MAVEN_BUILD_ENVIRONMENT /tmp/whitelisted-email-validator/target/whitelisted-email-validator.jar /opt/jboss/keycloak/standalone/deployments/whitelisted-email-validator.jar

# copy keycloak theme as fdk theme.
RUN cp -r /opt/jboss/keycloak/themes/keycloak /opt/jboss/keycloak/themes/fdk
RUN cp -r /opt/jboss/keycloak/themes/keycloak /opt/jboss/keycloak/themes/fdk-choose-provider
RUN cp -r /opt/jboss/keycloak/themes/keycloak /opt/jboss/keycloak/themes/fdk-fbh

# copy modified files from host ( 3 files) - trying to copy only changed files...
COPY themes/fdk /opt/jboss/keycloak/themes/fdk
COPY themes/fdk-choose-provider /opt/jboss/keycloak/themes/fdk-choose-provider
COPY themes/fdk-fbh /opt/jboss/keycloak/themes/fdk-fbh

COPY tools /opt/fdk/tools

# On service (re)start the stored keycloak state will be compared with the previously exported state, missing components will be restored.
# The restoration of the realms are ignored during startup if they already exist, an update script is run after startup to ensure they are completely up to date.
# When exporting state, it needs to be converted to a template file that has environment variable placeholders in it
# If needed (in dev environment) additional static realms can be included in imports.
COPY import /tmp/keycloak/import
COPY startup-scripts /opt/jboss/startup-scripts
COPY import-template /tmp/keycloak/import-template
USER root
RUN chmod o+w /tmp/keycloak/import/update
RUN chmod o+w /tmp/keycloak/import/overwrite
USER 1000

ENTRYPOINT [ "/opt/fdk/tools/preprocess-import-entrypoint.sh" ]

# port offset 4 is set because we want the server to be accessible both from host and from the sso container in local network claster.
# host name is made available by specifying it in the hosts file in host machine.
# port offset will cause changing port to 8084 which will be the same as exposed port to host.

CMD ["-b", "0.0.0.0", "-Dkeycloak.migration.action=import", "-Dkeycloak.migration.provider=dir", "-Dkeycloak.migration.dir=/tmp/keycloak/import/overwrite", "-Dkeycloak.migration.strategy=OVERWRITE_EXISTING", "-Djboss.socket.binding.port-offset=4"]
