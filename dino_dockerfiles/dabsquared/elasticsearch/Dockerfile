FROM docker.elastic.co/elasticsearch/elasticsearch:5.2.2

LABEL maintainer "dbrooks@dabsquared.com"

HEALTHCHECK CMD curl --fail "http://127.0.0.1:9200/_cat/health?h=status" || exit 1
