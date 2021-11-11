FROM openjdk:9-jre-slim

LABEL maintainer="petitviolet <mail@petitviolet.net>"
LABEL description="AWS DynamoDB local emulator"

WORKDIR /

RUN apt-get update && apt-get install -y curl

RUN curl -sS -L https://s3-ap-northeast-1.amazonaws.com/dynamodb-local-tokyo/dynamodb_local_latest.tar.gz | tar zxv

ENTRYPOINT ["java", "-Djava.library.path=./DynamoDBLocal_lib", "-jar", "DynamoDBLocal.jar"]

CMD ["-dbPath", "/data", "-sharedDb"]
