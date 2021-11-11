# Keep hub.Dockerfile aligned to this file as far as possible
ARG JAVA_OPTS="-Djava.security.egd=file:/dev/./urandom"
ARG APP_INSIGHTS_AGENT_VERSION=2.5.1

# Application image

FROM hmctspublic.azurecr.io/base/java:openjdk-11-distroless-1.4
LABEL maintainer="https://github.com/hmcts/org-role-mapping-service"

COPY lib/AI-Agent.xml /opt/app/
COPY build/libs/am-org-role-mapping-service.jar /opt/app/

EXPOSE 4098
CMD [ "am-org-role-mapping-service.jar" ]
