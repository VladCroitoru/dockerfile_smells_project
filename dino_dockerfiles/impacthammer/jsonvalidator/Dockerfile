FROM openjdk:alpine
 
EXPOSE 80

RUN apk add --no-cache maven
ADD src /jsonValidator/src
ADD pom.xml /jsonValidator/pom.xml
WORKDIR /jsonValidator
RUN mvn clean install -e
CMD mvn exec:java -e
