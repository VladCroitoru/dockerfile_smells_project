ARG APP_INSIGHTS_AGENT_VERSION=2.5.1
FROM hmctspublic.azurecr.io/base/java:openjdk-11-distroless-1.4
LABEL maintainer="https://github.com/hmcts/probate-back-office"

COPY lib/AI-Agent.xml /opt/app/
COPY build/libs/back-office.jar /opt/app/

EXPOSE 4104

CMD [ "back-office.jar" ]
