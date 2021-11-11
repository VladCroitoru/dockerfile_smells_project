FROM navikt/java:17
LABEL maintainer="Team Bidrag" \
      email="nav.ikt.prosjekt.og.forvaltning.bidrag@nav.no"

COPY src/main/resources/no features/no
COPY ./target/bidrag-cucumber-cloud-*.jar app.jar

EXPOSE 8080
