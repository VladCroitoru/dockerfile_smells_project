# Pull elasticsearch image
FROM barnybug/elasticsearch:1.4.1

# Install thrift plugin
RUN elasticsearch/bin/plugin -install elasticsearch/elasticsearch-transport-thrift/2.4.1

# Expose thrift port
EXPOSE 9500
