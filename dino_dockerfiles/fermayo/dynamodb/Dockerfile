FROM java:jre

ADD http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.tar.gz /tmp/dynamodb_local_latest.tar.gz
RUN mkdir -p /app && tar xvfz /tmp/dynamodb_local_latest.tar.gz -C /app/ && rm -f /tmp/dynamodb_local_latest.tar.gz
WORKDIR /app
EXPOSE 8000
VOLUME /data
CMD ["java", "-Djava.library.path=./DynamoDBLocal_lib", "-jar", "DynamoDBLocal.jar", "-dbPath", "/data"]
