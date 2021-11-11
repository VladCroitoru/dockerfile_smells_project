FROM maven:3.6-jdk-11 AS BUILD
# build indexer jar

COPY ./ /indexer
WORKDIR /indexer
RUN mvn -f goobi-viewer-indexer clean package


# start assembling the final image
FROM openjdk:11-jdk AS ASSEMBLE
LABEL org.opencontainers.image.authors="Matthias Geerdsen <matthias.geerdsen@intranda.com>"


ENV SOLR_URL http://solr:8983/solr/collection1
ENV VIEWER_URL http://viewer:8080/viewer

RUN mkdir -p /opt/digiverso/indexer

COPY --from=BUILD  /indexer/goobi-viewer-indexer/target/solr-Indexer.jar /usr/local/bin/solrIndexer.jar
COPY --from=BUILD  /indexer/goobi-viewer-indexer/src/main/resources/indexerconfig_solr.xml /opt/digiverso/indexer/solr_indexerconfig.xml
COPY ./docker/* /
RUN sed -e "s|<solrUrl>.*</solrUrl>|<solrUrl>${SOLR_URL}</solrUrl>|" -e 's|C:||g' -e "s|<viewerUrl>.*</viewerUrl>|<viewerUrl>${VIEWER_URL}</viewerUrl>|" -i /opt/digiverso/indexer/solr_indexerconfig.xml

# TODO: check for solr availability before start (wait-for-solr from solr image?)

CMD ["/run.sh"]