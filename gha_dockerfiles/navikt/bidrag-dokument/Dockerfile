FROM navikt/java:17
LABEL maintainer="Team Bidrag" \
      email="nav.ikt.prosjekt.og.forvaltning.bidrag@nav.no"

COPY ./target/app-exec.jar app.jar
COPY init-scripts /init-scripts

EXPOSE 8080
