# Pull base image.
FROM jainishshah17/oracle-java7

MAINTAINER jainish shah <jainish.shah@getzephyr.com>

# Install ElasticSearch.
RUN \
  cd /tmp && \
  wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.4.tar.gz && \
  tar xvzf elasticsearch-1.4.4.tar.gz && \
  rm -f elasticsearch-1.4.4.tar.gz && \
  mv /tmp/elasticsearch-1.4.4 /elasticsearch
RUN sudo /elasticsearch/bin/plugin -install elasticsearch/elasticsearch-cloud-aws/2.4.1

RUN echo "America/Los_Angeles" > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata


# Define mountable directories.
VOLUME ["/data"]
VOLUME ["/config"]


# Mount elasticsearch.yml config
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml
ADD run.sh /config/run.sh

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["sh /config/run.sh"]
CMD ["/elasticsearch/bin/elasticsearch"]

# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
EXPOSE 9200
EXPOSE 9300
EXPOSE 6200


