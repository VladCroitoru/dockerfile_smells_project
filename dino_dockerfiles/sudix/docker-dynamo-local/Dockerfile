FROM frolvlad/alpine-oraclejdk8

WORKDIR /var/dynamodb_wd

EXPOSE 8000

RUN apk add --no-cache openssl && \
    wget -O /var/dynamodb_wd/dynamodb_local_latest https://s3-us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.tar.gz && \
    tar xfz /var/dynamodb_wd/dynamodb_local_latest

ENTRYPOINT ["/usr/bin/java", "-Djava.library.path=.", "-jar", "DynamoDBLocal.jar", "-dbPath", "/var/dynamodb_local"]

CMD ["-port", "8000"]

VOLUME ["/var/dynamodb_local", "/var/dynamodb_wd"]
