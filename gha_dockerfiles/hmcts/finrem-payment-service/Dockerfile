ARG APP_INSIGHTS_AGENT_VERSION=2.5.1
FROM hmctspublic.azurecr.io/base/java:openjdk-11-distroless-1.4

COPY build/libs/finrem-payment-service.jar /opt/app/
COPY lib/AI-Agent.xml /opt/app/

EXPOSE 9001

CMD ["finrem-payment-service.jar"]
