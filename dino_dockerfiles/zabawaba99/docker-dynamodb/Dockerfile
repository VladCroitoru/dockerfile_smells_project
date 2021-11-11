FROM openjdk:8-jre

WORKDIR /var/dynamodb_wd
EXPOSE 8000

# setup dynamo
RUN curl -LO http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.tar.gz && \
	tar -xzf dynamodb_local_latest.tar.gz && \
	rm dynamodb_local_latest.tar.gz

ADD run.sh /run.sh

ENTRYPOINT ["/run.sh"]

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME ["/var/dynamodb_local", "/var/dynamodb_wd"]
