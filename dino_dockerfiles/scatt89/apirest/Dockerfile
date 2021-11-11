FROM ubuntu:14.04
MAINTAINER Marrarichy Da Silva Garcia <dasilvagarciam@gmail.com>
LABEL Description="APIrest docker image" Version="0.1"

#repository update and java 7 install
RUN apt-get -y update && \
apt-get install -y openjdk-7-jre-headless

#environment variables
ENV MYSQL_CONTAINER=db \
MYSQL_DATABASE=anuncios \
USERNAME=root \
PASS=root \
DLL-AUTO=create \
MYSQL-PORT=3306 \
JAVA_APP=app.jar

#add the jar app to the directory / of the cantainer
ADD $JAVA_APP /app.jar

#execute the copy jar file with the environment variables like parameters
CMD ["java", "-jar", "app.jar", "--spring.datasource.url=jdbc:mysql://${MYSQL_CONTAINER}:${MYSQL-PORT}/${MYSQL_DATABASE}", "--spring.jpa.hibernate.ddl-auto=${DLL-AUTO}", "--spring.datasource.username=${USERNAME}", "--spring.datasource.password=${PASS}"]

#expose the 8080 port of the container to the local host
EXPOSE 8080
