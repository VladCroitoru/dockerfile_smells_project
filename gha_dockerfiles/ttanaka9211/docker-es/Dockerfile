FROM docker.elastic.co/elasticsearch/elasticsearch:7.12.1

RUN elasticsearch-plugin install analysis-kuromoji && \
    elasticsearch-plugin install analysis-icu && \
    elasticsearch-plugin install --batch ingest-attachment
