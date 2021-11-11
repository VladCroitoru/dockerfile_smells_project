FROM navikt/java:11-appdynamics
ENV APPD_ENABLED=false
ENV APP_NAME=sykefravarsstatistikk-api
COPY import-vault-secrets.sh /init-scripts
COPY /target/sykefravarsstatistikk-api-0.0.1-SNAPSHOT.jar app.jar
