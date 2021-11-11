FROM navikt/java:11-appdynamics

ENV APPD_ENABLED=true

COPY java-debug.sh /init-scripts/08-java-debug.sh
COPY app/target/app.jar app.jar
