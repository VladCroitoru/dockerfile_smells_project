FROM hmctspublic.azurecr.io/base/java:openjdk-11-distroless-1.4
ARG APP_INSIGHTS_AGENT_VERSION=2.5.1

ENV APP pip-account-management.jar

COPY build/libs/$APP /opt/app/
COPY lib/AI-Agent.xml /opt/app/

EXPOSE 6969
CMD [ "pip-account-management.jar" ]
