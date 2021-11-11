#
# Kibana Dockerfile
#
# https://github.com/eliotk/docker-kibana
#

# Pull base image.
FROM dockerfile/java:oracle-java7

ENV KIBANA_VERSION 4.0.0-beta3

# Install Kibana
RUN \
  cd /tmp && \
  wget https://download.elasticsearch.org/kibana/kibana/kibana-$KIBANA_VERSION.tar.gz && \
  tar xvzf kibana-$KIBANA_VERSION.tar.gz && \
  rm -f kibana-$KIBANA_VERSION.tar.gz && \
  mv /tmp/kibana-$KIBANA_VERSION /kibana

# Mount kibana.yml config
ADD config/kibana.yml /kibana/config/kibana.yml

# Define default command.
CMD ["/kibana/bin/kibana"]

EXPOSE 5061
