FROM centos:latest
MAINTAINER Barry Gestwicki <barrygestwicki@gmail.com>

# Download and Logstash 1.4.2 and dependencies (notably Java/JRE)
RUN curl -O https://download.elasticsearch.org/logstash/logstash/packages/centos/logstash-1.4.2-1_2c0f5a1.noarch.rpm && \
    yum localinstall -y logstash-1.4.2-1_2c0f5a1.noarch.rpm

# Download and install Logstash Contrib plugins
RUN curl -O https://download.elasticsearch.org/logstash/logstash/packages/centos/logstash-contrib-1.4.2-1_efd53ef.noarch.rpm && \ 
    yum localinstall -y logstash-1.4.2-1_2c0f5a1.noarch.rpm

# Copy Logstash configuration file
ADD logstash.conf.d/ /etc/logstash/conf.d/

# Elasticsearch HTTP
EXPOSE 9200

# Elasticsearch transport
EXPOSE 9300

# Kibana
EXPOSE 9292

# Start logstash
ENTRYPOINT ["/etc/init.d/logstash"]
CMD ["start"]
