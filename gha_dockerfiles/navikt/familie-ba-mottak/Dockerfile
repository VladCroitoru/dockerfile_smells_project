FROM navikt/java:11-appdynamics

ENV APPD_ENABLED=true
ENV APP_NAME=familie-ba-mottak
ENV JAVA_OPTS="-XX:MaxRAMPercentage=75"

COPY ./target/familie-ba-mottak.jar "app.jar"
