FROM dockerfile/java:oracle-java7

ENV SOLRVERSION 4.4.0
ENV SOLR solr-$SOLRVERSION
RUN cd / && \
  wget https://archive.apache.org/dist/lucene/solr/$SOLRVERSION/$SOLR.zip && \
  unzip $SOLR.zip

VOLUME ["/solr"]
EXPOSE 8983
WORKDIR /$SOLR/example
CMD ["java", "-Dsolr.solr.home=/solr", "-jar", "start.jar"]
   
