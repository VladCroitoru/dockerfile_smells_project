FROM ubuntu:16.04

##### UBUNTU
# Update Ubuntu and add extra repositories
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install software-properties-common

# Install basic commands
RUN apt-get -y install links nano wget git curl

# Install Java
RUN apt-get -y install openjdk-8-jdk

# Install maven
ENV MAVEN_VERSION 3.3.9

RUN mkdir -p /usr/share/maven \
  && curl -fsSL http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
    | tar -xzC /usr/share/maven --strip-components=1 \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven

WORKDIR /code

# Prepare by downloading dependencies
ADD / /code/
#ADD * /code/
## NOTE: Not sure why this helps, but running install:help first makes the install:install-file command work
RUN mvn install:help
RUN mvn install:install-file -Dfile=/code/lib/org.sbgn-with-dependencies.jar -DgroupId=org.sbgn -DartifactId=org.sbgn-with-dependencies -Dversion=0.3 -Dpackaging=jar
#RUN mvn dependency:resolve
#RUN mvn verify
RUN mvn clean install

# Compile and package into a fat jar
RUN mvn clean package assembly:single

# Add relaxng files
ADD /src/main/resources/relaxng /relaxng

EXPOSE 4567
CMD ["java", "-jar", "/code/target/sbgn-validator-webservice-0.1-jar-with-dependencies.jar"]

