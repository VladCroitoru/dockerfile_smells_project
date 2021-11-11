from ubuntu:14.04
maintainer Alexis Morelle

# Prerequisites
run apt-get update

# Install Java 7
run apt-get install -y openjdk-7-jdk

# Install curl
RUN apt-get install -y curl

# Clean-up
RUN apt-get clean && rm -rf /var/lib/apt/lists

# Download Spatwork
RUN curl -Ls http://dl.bintray.com/almorelle/Spatwork/com/github/almorelle/spatwork/0.6.0/spatwork-0.6.0.jar

# Run
expose 8081

cmd ["java", "-jar", "spatwork-0.6.0.jar", "-Drestx.mode=prod"]