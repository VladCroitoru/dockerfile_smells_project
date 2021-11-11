FROM ubuntu:latest
MAINTAINER Horace Heaven "hheaven@medullan.com"

# Import MongoDB public GPG key AND create a MongoDB list file
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10

RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/10gen.list

# Update software package
RUN apt-get -y update

# Install ssh server
RUN apt-get -y install openssh-server

# Install java
RUN apt-get -y install default-jdk

# Install nodejs programs TODO: update to use mongo-client
RUN apt-get -y install nodejs nodejs-legacy npm mongodb-org

# Install mocha
RUN npm install -g mocha

# Change the root user's password
RUN echo "root:password" | chpasswd

# Adds the jenkins user and change the password
RUN adduser jenkins
RUN echo "jenkins:jenkins" | chpasswd

# Configure ssh
RUN rm /etc/ssh/ssh_host_rsa_key
RUN mkdir -p /var/run/sshd
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd

EXPOSE 22

CMD ["/usr/sbin/sshd -D"]
