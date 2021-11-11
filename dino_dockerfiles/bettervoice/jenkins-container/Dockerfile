# Jenkins.

FROM ubuntu:14.04
MAINTAINER Thomas Quintana <thomas@bettervoice.com>

# Install Dependencies.
RUN apt-get update && apt-get install -y git-core npm wget
RUN ln -s /usr/bin/nodejs /usr/bin/node

# Install Jenkins.
RUN wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
RUN sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
RUN apt-get update && apt-get install -y jenkins

# Install JS stuff.
RUN npm install -g bower
RUN npm install -g grunt
RUN npm install -g grunt-cli

# Open the container up to the world.
EXPOSE 8080/tcp

# Start Jenkins.
CMD service jenkins start && tail -F /var/log/jenkins/jenkins.log
