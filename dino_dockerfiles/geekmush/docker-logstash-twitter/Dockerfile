#
# LogStash Dockerfile
#
# https://github.com/geekmush/logstash-twitter
#

# Pull base image.
FROM dockerfile/java

# Install LogStash.
RUN \
  cd /tmp && \
  wget https://download.elasticsearch.org/logstash/logstash/logstash-1.4.2.tar.gz && \
  tar xvzf logstash-1.4.2.tar.gz && \
  rm -f logstash-1.4.2.tar.gz && \
  mv /tmp/logstash-1.4.2 /logstash
  

# Define mountable directories.
VOLUME ["/data"]

# Mount logstash.yml config
ADD config/logstash.in /logstash/config/logstash.in
ADD bin/init.sh /logstash/bin/init.sh
ADD fix/logstash/lib/logstash/pipeline.rb /logstash/lib/logstash/pipeline.rb

# Define working directory.
WORKDIR /data

# Define default command.
#CMD ["/elasticsearch/bin/elasticsearch"]
CMD ["/logstash/bin/init.sh"]

# Expose ports.
#   - 9200: HTTP
#   - 9300: transport
#EXPOSE 9200
#EXPOSE 9300
