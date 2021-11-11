FROM maven:3.5.0-jdk-7
ADD https://github.com/awslabs/dynamodb-cross-region-library/archive/1.2.1.tar.gz /usr/src/
RUN tar xzvf /usr/src/1.2.1.tar.gz -C /usr/src/
RUN cd /usr/src/dynamodb-cross-region-library-1.2.1 && mvn install
ENTRYPOINT ["java", "-jar", "/usr/src/dynamodb-cross-region-library-1.2.1/target/dynamodb-cross-region-replication-1.2.1.jar"]