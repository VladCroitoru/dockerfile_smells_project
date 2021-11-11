FROM anapsix/alpine-java:jdk8

MAINTAINER AlexLee <alexlee7171@gmail.com>

# Update and install all of the required packages.
# At the end, remove the apk cache
RUN apk upgrade --update && \
	apk add --update curl wget ca-certificates && \
    rm -rf /var/cache/apk/*

# Install Elasticsearch 2.3.3
RUN wget https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.3.3/elasticsearch-2.3.3.tar.gz && \
	tar zxvf elasticsearch-2.3.3.tar.gz && \
	rm elasticsearch-2.3.3.tar.gz && \
	mv elasticsearch-2.3.3 elasticsearch 

# Define mountable directories.
VOLUME ["/data"]

# Mount elasticsearch.yml config
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["/elasticsearch/bin/elasticsearch", "-Des.insecure.allow.root=true", "-Des.network.host=0.0.0.0"]

# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
EXPOSE 9200
EXPOSE 9300