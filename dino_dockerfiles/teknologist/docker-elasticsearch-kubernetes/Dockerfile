FROM quay.io/pires/docker-elasticsearch:1.7.2

MAINTAINER teknologist@gmail.com

# Override elasticsearch.yml config, otherwise plug-in install will fail
ADD do_not_use.yml /elasticsearch/config/elasticsearch.yml

# Install Elasticsearch plug-ins
RUN /elasticsearch/bin/plugin -i io.fabric8/elasticsearch-cloud-kubernetes/1.3.0 --verbose
RUN /elasticsearch/bin/plugin -i mobz/elasticsearch-head --verbose
RUN /elasticsearch/bin/plugin -i polyfractal/elasticsearch-inquisitor --verbose
RUN /elasticsearch/bin/plugin -i com.github.richardwilly98.elasticsearch/elasticsearch-river-mongodb/2.0.9  --verbose
RUN /elasticsearch/bin/plugin -i elasticsearch/elasticsearch-analysis-kuromoji/2.7.0 --verbose
RUN /elasticsearch/bin/plugin -i elasticsearch/elasticsearch-analysis-phonetic/2.7.0 --verbose
RUN /elasticsearch/bin/plugin -i royrusso/elasticsearch-HQ --verbose

# Override elasticsearch.yml config, otherwise plug-in install will fail
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml

# Copy run script
COPY run.sh /
