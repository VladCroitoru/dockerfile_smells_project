############################################################
# Dockerfile to run java & nodejs based web apps
# Based on phusion Image
############################################################

FROM phusion/baseimage:0.9.17
MAINTAINER Rasheed Amir <rasheed@aurorasolutions.io>

# make sure the package repository is up to date
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN apt-get -y update

# install python-software-properties (so you can do add-apt-repository)
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-software-properties software-properties-common

#---------- JAVA

# install oracle java 8 from PPA
RUN add-apt-repository ppa:webupd8team/java -y
RUN apt-get update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get -y install oracle-java8-installer && apt-get clean

# set oracle java as the default java
RUN update-java-alternatives -s java-8-oracle
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc

#---------- Utilities

# install utilities
RUN apt-get -y install vim nano git sudo zip bzip2 fontconfig curl

#---------- Maven

# install maven
RUN apt-get -y install maven

#---------- Gradle

# install gradle
RUN add-apt-repository ppa:cwchien/gradle
RUN apt-get update
RUN apt-get -y install gradle

#---------- NodeJs

# install node.js from PPA
#RUN add-apt-repository ppa:chris-lea/node.js

# Note the new setup script name for Node.js v0.12
RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -

RUN apt-get update

RUN apt-get -y install nodejs

#---------- npm

# update npm to the latest version
RUN npm update -g npm

#---------- Yoeman

# install yeoman
RUN npm install -g yo

#---------- Bower

# install bower
RUN npm install -g bower

#---------- Grunt

# install grunt
RUN npm install -g grunt-cli

#---------- Gulp

# install grunt
RUN npm install -g gulp

#---------- Compass

RUN apt-get install -y -f ruby-compass
RUN gem install compass

#---------- Configure Users

# configure the "aurora" and "root" users
RUN echo 'root:aurora' |chpasswd
RUN groupadd aurora && useradd aurora -s /bin/bash -m -g aurora -G aurora && adduser aurora sudo
RUN echo 'aurora:aurora' |chpasswd
RUN cd /home && chown -R aurora:aurora /home/aurora

#---------- Expose

# expose the working directory
VOLUME ["/home/aurora"]

# expose the tomcat port
EXPOSE 8080

# expose the grunt server port
EXPOSE 9000

# expose the gulp port
EXPOSE 35729

# expose the the SSHD port
EXPOSE 22

# SSHD

# Baseimage-docker disables the SSH server by default. Add the following to your Dockerfile to enable it:
RUN rm -f /etc/service/sshd/down

# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

CMD /usr/sbin/sshd -D