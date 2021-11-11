FROM navikt/java:11-appdynamics

COPY build/libs/eessi-pensjon-prefill.jar /app/app.jar
COPY nais/export-vault-secrets.sh /init-scripts/

ENV APPD_NAME eessi-pensjon
ENV APPD_TIER prefill
ENV APPD_ENABLED true
