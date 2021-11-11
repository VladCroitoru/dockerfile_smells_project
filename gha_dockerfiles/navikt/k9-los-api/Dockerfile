FROM navikt/java:16-appdynamics
ENV APPD_ENABLED=true
LABEL org.opencontainers.image.source=https://github.com/navikt/k9-los-api

ENV JAVA_OPTS="-XX:MaxRAMPercentage=75.0 -Djava.security.egd=file:/dev/./urandom -Duser.timezone=Europe/Oslo "

COPY build/libs/app.jar ./
COPY build/resources/main/scripts /init-scripts/.


