FROM openjdk:16-slim AS builder

ARG BUILD_NUMBER
ENV BUILD_NUMBER ${BUILD_NUMBER:-1_0_0}

WORKDIR /app
ADD . .
RUN ./gradlew assemble -Dorg.gradle.daemon=false

FROM adoptopenjdk/openjdk16:alpine-jre
LABEL maintainer="HMPPS Digital Studio <info@digital.justice.gov.uk>"

RUN apk upgrade --no-cache && \
    apk add --no-cache \
      curl \
      tzdata

ENV TZ=Europe/London
RUN ln -snf "/usr/share/zoneinfo/$TZ" /etc/localtime && echo "$TZ" > /etc/timezone

RUN addgroup --gid 2000 --system appgroup && \
    adduser --uid 2000 --system appuser && \
    adduser appuser appgroup

WORKDIR /app
COPY --from=builder --chown=appuser:appgroup /app/build/libs/hmpps-delius-interventions-event-listener*.jar /app/app.jar
COPY --from=builder --chown=appuser:appgroup /app/build/libs/applicationinsights-agent*.jar /app/agent.jar
COPY --from=builder --chown=appuser:appgroup /app/applicationinsights.json /app
COPY --from=builder --chown=appuser:appgroup /app/applicationinsights.dev.json /app

USER 2000

ARG BUILD_NUMBER
ENV BUILD_NUMBER ${BUILD_NUMBER:-1_0_0}

ENTRYPOINT ["java", "-javaagent:/app/agent.jar", "-jar", "/app/app.jar"]
