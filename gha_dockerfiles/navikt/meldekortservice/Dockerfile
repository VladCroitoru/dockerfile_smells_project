FROM navikt/java:11
COPY --chown=apprunner:root export-vault-creds.sh /init-scripts/03-export-vault-creds.sh
RUN chmod a+x /init-scripts/03-export-vault-creds.sh
COPY build/libs/meldekortservice-all.jar /app/app.jar
EXPOSE 8090