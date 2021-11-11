FROM jimschubert/8-jdk-alpine-mvn:1.0
MAINTAINER sumeet rohatgi

RUN apk add --update curl git 
RUN git clone https://github.com/swagger-api/swagger-codegen.git && ls -l swagger-codegen
WORKDIR swagger-codegen
RUN mvn package
RUN apk add --update bash
COPY generate-java-lib.sh /usr/local/bin
