FROM openjdk:8-jre
MAINTAINER milanvojnovic@gmail.com
RUN apt-get update
RUN wget http://central.maven.org/maven2/io/github/azagniotov/stubby4j/5.0.1/stubby4j-5.0.1.jar
COPY api_stub /usr/local/api_stub
EXPOSE 8882
CMD java -jar stubby4j-5.0.1.jar -l 0.0.0.0 -w --data /usr/local/api_stub/api_stub.yaml
HEALTHCHECK CMD curl --fail http://127.0.0.1:8882/hello-world || exit 1