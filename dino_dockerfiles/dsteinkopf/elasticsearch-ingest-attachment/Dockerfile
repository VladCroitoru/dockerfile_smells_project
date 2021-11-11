# FROM elasticsearch
# this image on docker hub was deprecated for some time (see https://hub.docker.com/_/elasticsearch/)
# and still seems "weird" to me. So I am using one from elastic directly
# (see https://www.docker.elastic.co/r/elasticsearch/elasticsearch)
FROM docker.elastic.co/elasticsearch/elasticsearch:6.8.15

RUN bin/elasticsearch-plugin install  --batch ingest-attachment

