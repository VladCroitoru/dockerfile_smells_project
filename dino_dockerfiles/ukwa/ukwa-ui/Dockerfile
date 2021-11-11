FROM maven:3-jdk-8 AS build-env

# Build under maven
MAINTAINER Mindaugas Vidmantas "mindaugas.vidmantas@bl.uk"

COPY pom.xml /ukwa-ui/pom.xml
COPY src /ukwa-ui/src

RUN cd /ukwa-ui/ && \
  mvn package -q -DskipTests

FROM openjdk:8-jre

COPY --from=build-env /ukwa-ui/target/marsspiders-ukwa-*.war /ukwa-ui.war

ENV ARCHIVE_WEB_LOCATION="https://www.webarchive.org.uk/wayback/archive/" \
 SOLR_COLLECTION_SEARCH_PATH="https://beta.webarchive.org.uk/solr/collections/select" \
 SOLR_FULL_TEXT_SEARCH_PATH="https://beta.webarchive.org.uk/ukwa/search" \
 SOLR_READ_TIMEOUT="60000" \
 SOLR_CONNECTION_TIMEOUT="60000" \
 SOLR_SHOW_STUB_DATA_SERVICE_NOT_AVAILABLE="true" \
 SOLR_USERNAME="" \
 SOLR_PASSWORD="" \
 SOLR_SHOW_STUB_DATA_SERVICE_NOT_AVAILABLE="false" \
 BL_SMTP_SERVER_HOST="mailhost" \
 BL_SMTP_USERNAME="mailuser" \
 BL_SMTP_PASSWORD="mailpassword"

ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/ukwa-ui.war"]
EXPOSE 8080
