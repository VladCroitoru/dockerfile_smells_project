ARG APP_INSIGHTS_AGENT_VERSION=2.5.1
FROM hmctspublic.azurecr.io/base/java:openjdk-11-distroless-1.4 as base
LABEL maintainer="https://github.com/hmcts/ethos-repl-docmosis-service"

COPY lib/AI-Agent.xml /opt/app/
COPY build/libs/ethos-repl-docmosis-service.jar /opt/app/

FROM debian:10 AS builder

USER root
RUN apt update
RUN apt install --yes libharfbuzz-dev
USER hmcts

FROM base

COPY --from=builder /usr/lib/x86_64-linux-gnu/libharfbuzz.so.0 /usr/lib/x86_64-linux-gnu/libharfbuzz.so.0
COPY --from=builder /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0 /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0
COPY --from=builder /usr/lib/x86_64-linux-gnu/libgraphite2.so.3 /usr/lib/x86_64-linux-gnu/libgraphite2.so.3
COPY --from=builder /lib/x86_64-linux-gnu/libpcre.so.3 /lib/x86_64-linux-gnu/libpcre.so.3

EXPOSE 8081

CMD ["ethos-repl-docmosis-service.jar"]
