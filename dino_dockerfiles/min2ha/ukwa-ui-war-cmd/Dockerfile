FROM openjdk:8-jre-alpine
MAINTAINER Mindaugas Vidmantas "mindaugas.vidmantas@bl.uk"
ENV SOLR_COLLECTION_SEARCH_PATH="http://192.168.45.241:8983/solr/collections/select?"
ENV SOLR_FULL_TEXT_SEARCH_PATH="http://devsolr-proxy:8983/solr/all/select?"
ENV SOLR_READ_TIMEOUT="6000"
ENV SOLR_CONNECTION_TIMEOUT="6000"
ENV SOLR_SHOW_STUB_DATA_SERVICE_NOT_AVAILABLE="true"
ENV SOLR_USERNAME="none"
ENV SOLR_PASSWORD="none"
COPY ./ukwa-ui-1.4.2.RELEASE.war /ROOT.war
ENTRYPOINT ["/usr/bin/java"]
CMD ["-jar", "/ROOT.war"]
EXPOSE 8080
