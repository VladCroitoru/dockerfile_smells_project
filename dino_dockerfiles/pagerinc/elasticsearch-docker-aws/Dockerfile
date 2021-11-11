FROM docker.elastic.co/elasticsearch/elasticsearch:5.3.0
LABEL maintainer william@pager.com

WORKDIR /usr/share/elasticsearch
USER elasticsearch

# Install AWS plugins
RUN eval ${ES_JAVA_OPTS:-} elasticsearch-plugin install --batch discovery-ec2 \
 && eval ${ES_JAVA_OPTS:-} elasticsearch-plugin install --batch repository-s3
