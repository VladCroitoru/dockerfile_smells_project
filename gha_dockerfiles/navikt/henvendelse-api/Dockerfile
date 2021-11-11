FROM navikt/java:11-appdynamics

ENV APPD_ENABLED=true

COPY java-debug.sh /init-scripts/08-java-debug.sh
COPY /target/henvendelse-api.jar app.jar
