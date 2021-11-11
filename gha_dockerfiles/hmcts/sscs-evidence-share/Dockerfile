ARG APP_INSIGHTS_AGENT_VERSION=2.6.1
FROM hmctspublic.azurecr.io/base/java:openjdk-11-distroless-1.4

COPY lib/AI-Agent.xml /opt/app/
COPY build/libs/sscs-evidence-share.jar /opt/app/

EXPOSE 8091

CMD ["sscs-evidence-share.jar"]
