FROM java
RUN mkdir /dynamodb
RUN cd /dynamodb/ && wget http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.tar.gz
RUN cd /dynamodb/ && tar zxf dynamodb_local_latest.tar.gz
ENTRYPOINT ["/usr/bin/java", "-Djava.library.path=/dynamodb/DynamoDBLocal_lib", "-jar", "/dynamodb/DynamoDBLocal.jar"]
CMD ["-help"]
