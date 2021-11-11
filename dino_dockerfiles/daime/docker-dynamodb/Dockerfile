FROM java:jre

WORKDIR /opt/dynamodb

RUN wget -O /opt/dynamodb/dynamodb_local_latest http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest
RUN tar xfz /opt/dynamodb/dynamodb_local_latest

VOLUME ["/var/lib/dynamodb"]

EXPOSE 4761

CMD ["/usr/bin/java", "-Djava.library.path=./DynamoDBLocal_lib", "-jar", "DynamoDBLocal.jar", "-dbPath", "/var/lib/dynamodb", "-port", "4761"]
