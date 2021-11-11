ARG APP_INSIGHTS_AGENT_VERSION=2.5.1

FROM hmctspublic.azurecr.io/base/java:openjdk-11-distroless-1.4

COPY build/libs/rpa-em-ccd-orchestrator.jar lib/applicationinsights-agent-2.5.1.jar lib/AI-Agent.xml /opt/app/

HEALTHCHECK --interval=10s --timeout=10s --retries=10 CMD http_proxy="" wget -q --spider http://localhost:8080/health || exit 1

CMD ["rpa-em-ccd-orchestrator.jar"]

EXPOSE 8080