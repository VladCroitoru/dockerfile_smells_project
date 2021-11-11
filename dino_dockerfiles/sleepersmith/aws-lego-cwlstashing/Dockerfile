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
RUN ./bin/plugin install logstash-input-kinesis && \
    ./bin/plugin install logstash-output-elasticsearch

# Add files
ADD worker.rb ./vendor/bundle/jruby/1.9/gems/logstash-input-kinesis-1.4.3-java/lib/logstash/inputs/kinesis/
ADD ls-aws-cwl.conf ./
ADD aws-log-init.sh ./
RUN chmod +x ./aws-log-init.sh

# Create user and assign permission
ENTRYPOINT ["/home/local/aws-log-init.sh"]
