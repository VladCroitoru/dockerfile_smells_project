FROM docker.elastic.co/elasticsearch/elasticsearch:6.3.0

USER elasticsearch
RUN bin/elasticsearch-plugin install -b analysis-icu || true
