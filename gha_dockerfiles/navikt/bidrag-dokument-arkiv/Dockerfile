FROM navikt/java:17
LABEL maintainer="Team Bidrag" \
      email="nav.ikt.prosjekt.og.forvaltning.bidrag@nav.no"

COPY init-scripts /init-scripts
ADD ./target/bidrag-dokument-arkiv*.jar app.jar

EXPOSE 8080
