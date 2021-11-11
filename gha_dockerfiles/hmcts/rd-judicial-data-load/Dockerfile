ARG APP_INSIGHTS_AGENT_VERSION=2.6.1
FROM hmctspublic.azurecr.io/base/java:openjdk-11-distroless-1.4

# Mandatory!
ENV APP rd-judicial-data-load.jar
ENV APPLICATION_TOTAL_MEMORY 512M
ENV APPLICATION_SIZE_ON_DISK_IN_MB 48

# Optional
ENV JAVA_OPTS ""

#COPY lib/applicationinsights-agent-2.5.1-BETA.jar lib/AI-Agent.xml /opt/app/
COPY build/libs/$APP /opt/app/

WORKDIR /opt/app

EXPOSE 8090

CMD [ "rd-judicial-data-load.jar" ]

