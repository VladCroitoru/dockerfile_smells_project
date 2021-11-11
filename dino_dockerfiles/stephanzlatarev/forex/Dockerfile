FROM java:7

MAINTAINER Stephan Zlatarev

# Install Maven and Git
RUN apt-get update
RUN apt-get install -y maven

# Fetch the application and package it into an executable jar
RUN git clone https://github.com/stephanzlatarev/forex.git /root/forex
WORKDIR /root/forex
RUN mvn package

# Prepare docker container for start up
EXPOSE 8080
ENTRYPOINT java -jar target/forex-1.0.0.jar
