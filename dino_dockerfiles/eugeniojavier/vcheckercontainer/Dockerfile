#docker run --rm -v $PWD:/usr/src/kurento-java -w /usr/src/kurento-java -t maven:3.2-jdk-7 
FROM maven:3.3-jdk-7
MAINTAINER Javier Cabezas Gívica y Eugenio F. González Martín 

#Environment variable with repositories text file
ENV REPOSITORIES config.json
#Environment variable with java jar file
ENV JAVAJAR VChecker-0.0.1-SNAPSHOT.jar

# Copying the work directory into /usr/src/mymaven/

ADD $PWD /usr/src/mymaven/


# Placing us in this directory
WORKDIR /usr/src/mymaven

#
# Set up of required permissions on script file and VChecker file 
#

RUN chmod 777 $JAVAJAR

ENTRYPOINT java -jar $JAVAJAR $REPOSITORIES


