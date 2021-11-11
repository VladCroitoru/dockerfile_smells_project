FROM java:8
ARG LS_TAR_NAME=logstash-2.2.2
ARG LS_TAR_URL=https://download.elastic.co/logstash/logstash/

# Create directory
RUN mkdir /home/local
WORKDIR /home/local

# Download
RUN wget ${LS_TAR_URL}${LS_TAR_NAME}.tar.gz && \
    tar --strip-components 1 -xvf ${LS_TAR_NAME}.tar.gz && \
    rm ${LS_TAR_NAME}.tar.gz

# Install plugins
RUN ./bin/plugin install logstash-input-s3 && \
    ./bin/plugin install logstash-output-elasticsearch && \
	./bin/plugin install logstash-filter-fingerprint

# Add files
ADD s3.rb ./vendor/bundle/jruby/1.9/gems/logstash-input-s3-2.0.4/lib/logstash/inputs/
ADD ls-aws-sqs3.conf ./
ADD aws-log-init.sh ./
RUN chmod +x ./aws-log-init.sh && \
	mkdir /home/local/temp && \
	chmod 666 /home/local/temp

# Create user and assign permission
#ENTRYPOINT ["/home/local/aws-log-init.sh"]
