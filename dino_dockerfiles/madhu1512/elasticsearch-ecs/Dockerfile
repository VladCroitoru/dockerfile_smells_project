FROM elasticsearch:5.2.0-alpine
MAINTAINER Madhukar Thota <madhukar.thota@gmail.com>
WORKDIR /usr/share/elasticsearch

# Install EC2 Discovery Plugin
RUN bin/elasticsearch-plugin install --batch discovery-ec2

COPY docker-entrypoint.sh /docker-entrypoint.sh
