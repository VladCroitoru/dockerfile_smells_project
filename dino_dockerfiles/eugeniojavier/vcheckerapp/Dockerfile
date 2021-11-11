
FROM ubuntu:14.04

MAINTAINER Javier Cabezas Gívica y Eugenio F. González Martín 

#Environment variable with the folder on which the jar file will be copied in the container and the jar name

ENV JARPATHFILE /usr/bin/VCheckerApp-0.0.1-SNAPSHOT-jar-with-dependencies.jar

#Environment variable with the jar path

ENV JARPATH usr/bin

#Environment variable to define the json input file

ENV CONFIGJSON config.json

# Copying the contents of the current directory to the container

COPY $PWD $JARPATH

# Starting with the installations required to use this container as an artifact checker

# Updating packages

RUN apt-get update

# Installing Java

RUN apt-get  install -y openjdk-7-jre-headless 

# Installing NPM

RUN apt-get install -y nodejs

RUN apt-get install -y npm

# Installing Bower

RUN npm install -g bower

# Creating the commmand to be executed

CMD java -jar $JARPATHFILE $CONFIGJSON

