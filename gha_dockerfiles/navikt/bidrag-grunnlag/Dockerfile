FROM navikt/java:17
LABEL maintainer="Team Bidrag" \
      email="bidrag@nav.no"

COPY ./target/bidrag-grunnlag-*.jar app.jar
COPY --from=redboxoss/scuttle:latest /scuttle /bin/scuttle

EXPOSE 8080

ENV ENVOY_ADMIN_API=http://127.0.0.1:15000