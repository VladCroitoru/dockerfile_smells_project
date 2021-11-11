FROM entando/entando-ubi8-java11-base:6.4.0
ARG VERSION
### Required OpenShift Labels
LABEL name="Entando Component Manager" \
      maintainer="dev@entando.com" \
      vendor="Entando Inc." \
      version="v{VERSION}" \
      release="6.3.0" \
      summary="Entando Component Manager for Entando Component Repository" \
      description="The component manager provides apis and infrastructure to support the deployment and development of bundles to an Entando Application."

COPY target/generated-resources/licenses /licenses

ENV PORT=8080 \
    CLASSPATH=/opt/lib \
    USER_NAME=root \
    NSS_WRAPPER_PASSWD=/tmp/passwd \
    NSS_WRAPPER_GROUP=/tmp/group

COPY passwd.template entrypoint.sh /

EXPOSE 8080


# copy pom.xml and wildcards to avoid this command failing if there's no target/lib directory
COPY pom.xml target/lib* /opt/lib/

# NOTE we assume there's only 1 jar in the target dir
# but at least this means we don't have to guess the name
# we could do with a better way to know the name - or to always create an app.jar or something
COPY target/entando-component-manager.jar /opt/app.jar
WORKDIR /opt
ENTRYPOINT ["/entrypoint.sh"]
CMD ["java", "-XX:MaxRAMPercentage=80.0", "-jar", "app.jar"]
