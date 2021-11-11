FROM openjdk:latest

LABEL maintainer="kterada.0509sg@gmail.com"

RUN set -x \
    # System update
    && apt-get update \
    # Install wget
    && apt-get install -y wget \
    # Cleanup apt cache
    && apt-get clean \
    # Create Directory
    && mkdir -p /usr/local/dynamodb-local \
    && cd /usr/local/dynamodb-local \
    # Get dynamodb local file & Decompression
    && wget http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.tar.gz \
    && tar zxvf dynamodb_local_latest.tar.gz \
    # Create Database directory
    && mkdir -p /usr/local/dynamodb-local/db

CMD ["java", "-Djava.library.path=/usr/local/dynamodb-local/DynamoDBLocal_lib", "-jar", "/usr/local/dynamodb-local/DynamoDBLocal.jar", "-port", "8080", "-dbPath", "/usr/local/dynamodb-local/db"]
EXPOSE 8080
