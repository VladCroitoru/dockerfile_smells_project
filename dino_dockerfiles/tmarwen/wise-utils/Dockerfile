#
# Java 1.6 & Maven Dockerfile
#

# pull base image.
FROM dockerfile/java:oracle-java6

# maintainer details
MAINTAINER Marwen Trabelsi "marwen.trabelsi.insat@gmail.com"

# update packages and install maven
RUN  \
  export DEBIAN_FRONTEND=noninteractive && \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y vim wget curl git maven
  
# Clone project
run git clone https://github.com/tmarwen/wise-utils.git

# Build project
run cd wise-utils/standalone && mvn clean install

# create working directory
WORKDIR ./target

# Define default command.
CMD ["bash"]
