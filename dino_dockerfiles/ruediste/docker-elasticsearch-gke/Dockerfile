FROM quay.io/pires/docker-elasticsearch-kubernetes:5.1.2
MAINTAINER Ruedi Steinmann
RUN export CLUSTER_NAME=mycluster \
&& /elasticsearch/bin/elasticsearch-plugin install repository-gcs
