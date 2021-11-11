FROM elasticsearch:5.0.0

# Install plugins
RUN ./bin/elasticsearch-plugin install discovery-ec2 --batch && \
    ./bin/elasticsearch-plugin install repository-s3 --batch
	
ADD limits.conf /etc/security/
ADD elasticsearch.yml ./config/