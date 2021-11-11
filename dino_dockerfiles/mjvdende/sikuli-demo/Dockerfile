# Pull base image.
FROM dockerfile/java:oracle-java7

# Setup Software dependencies 
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -
RUN apt-get update 

RUN apt-get install -y maven git curl build-essential nodejs 

# Nodejs tooling
RUN npm install -g grunt-cli bower
