FROM navikt/java:11
COPY --from=redboxoss/scuttle:latest /scuttle /bin/scuttle

ENV ENVOY_ADMIN_API=http://127.0.0.1:15000
ENV ISTIO_QUIT_API=http://127.0.0.1:15020

ENV APP_NAME=familie-ef-sak
ENV JAVA_OPTS="-XX:MaxRAMPercentage=75"
COPY ./target/familie-ef-sak.jar "app.jar"

ENTRYPOINT ["scuttle", "/dumb-init", "--", "/entrypoint.sh"]