# Docker Definition for ElasticSearch Curator

FROM python:3.6.5-slim
MAINTAINER Matthew Ralph (mralph@equalexperts.com)

RUN useradd -m curator
RUN pip install elasticsearch-curator==5.5
RUN mkdir -p /etc/elasticsearch-curator

USER curator
COPY curator.yaml /etc/elasticsearch-curator
COPY actions.yaml /etc/elasticsearch-curator

ENTRYPOINT [ "/usr/local/bin/curator" ]
CMD ["--config", "/etc/elasticsearch-curator/curator.yaml", "/etc/elasticsearch-curator/actions.yaml"]
