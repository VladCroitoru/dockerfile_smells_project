FROM quay.io/pires/docker-elasticsearch:2.3.3

MAINTAINER pjpires@gmail.com

# Override elasticsearch.yml config, otherwise plug-in install will fail
ADD do_not_use.yml /elasticsearch/config/elasticsearch.yml

# Install Elasticsearch plug-ins
RUN /elasticsearch/bin/plugin install io.fabric8/elasticsearch-cloud-kubernetes/2.3.3 --verbose --batch
RUN /elasticsearch/bin/plugin install https://github.com/jaohaohsuan/elasticsearch-analysis-ik/releases/download/v2.3.3-beta.1/elasticsearch-analysis-ik-1.9.3.zip --verbose --batch
RUN /elasticsearch/bin/plugin install delete-by-query

# Override elasticsearch.yml config, otherwise plug-in install will fail
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml
ADD logging.yml /elasticsearch/config/logging.yml

VOLUME ["/snapshot/backups"]
# Copy run script
COPY run.sh /
