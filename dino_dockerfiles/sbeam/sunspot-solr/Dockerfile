FROM solr:6

USER root

COPY *.xml ./

# test env
RUN mkdir -p server/solr/test/conf
RUN cp schema.xml server/solr/test/conf/
RUN cp solrconfig.xml server/solr/test/conf/

# dev env
RUN mkdir -p server/solr/development/conf
RUN cp schema.xml server/solr/development/conf/
RUN cp solrconfig.xml server/solr/development/conf/

# staging env
RUN mkdir -p server/solr/staging/conf
RUN cp schema.xml server/solr/staging/conf/
RUN cp solrconfig.xml server/solr/staging/conf/

# production env
RUN mkdir -p server/solr/production/conf
RUN cp schema.xml server/solr/production/conf/
RUN cp solrconfig.xml server/solr/production/conf/

RUN chown -R solr server/solr

USER solr
