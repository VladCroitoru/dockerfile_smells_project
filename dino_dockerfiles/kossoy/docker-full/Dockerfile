# DOCKER-VERSION 0.7.1
FROM      ubuntu:14.04
MAINTAINER Oleg Kossoy <oleg@kossoy.com>
# thanks to Julien Dubois <julien.dubois@gmail.com>

# compass
RUN apt-get update -qq

# install ruby
RUN apt-get install -y -qq ruby-dev
RUN apt-get install make

# install compass
RUN gem install --no-rdoc --no-ri compass

# make sure the package repository is up to date
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN apt-get -y update

# install python-software-properties (so you can do add-apt-repository)
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-software-properties software-properties-common

# install SSH server so we can connect multiple times to the container
RUN apt-get -y install openssh-server && mkdir /var/run/sshd

# install oracle java from PPA
RUN add-apt-repository ppa:webupd8team/java -y
RUN apt-get update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get -y install oracle-java8-installer && apt-get clean

# Set oracle java as the default java
RUN update-java-alternatives -s java-8-oracle
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc

# install utilities
RUN apt-get -y install vim git sudo zip bzip2 fontconfig curl mc

# install maven
RUN apt-get -y install maven

# install node.js from PPA
RUN add-apt-repository ppa:chris-lea/node.js
RUN apt-get update
RUN apt-get -y install nodejs

# install yeoman
RUN npm install -g yo

# install JHipster, angular and express
RUN npm install -g grunt-cli bower
RUN npm install -g generator-jhipster@1.10.1
RUN npm install -g generator-angular
RUN npm install -g express-generator
RUN npm install -g http-server

# configure the "devel" and "root" users
RUN echo 'root:devel' |chpasswd
RUN groupadd devel && useradd devel -s /bin/bash -m -g devel -G devel && adduser devel sudo
RUN echo 'devel:devel' |chpasswd

# expose the working directory, the Tomcat port, the Grunt server port, the SSHD port, and run SSHD
VOLUME ["/devel"]
EXPOSE 3000
EXPOSE 8080
EXPOSE 9000
EXPOSE 22
CMD    /usr/sbin/sshd -D


# sudo docker run -v ~/devel:/devel -p 3000:3000 -p 8080:8080 -p 9000:9000 -p 35729:35729 -p 2222:22 -t kossoy/devel
# cat ~/.ssh/id_rsa.pub | ssh -p 2222 devel@localhost 'mkdir ~/.ssh && cat >> ~/.ssh/authorized_keys'

# docker cleanup -->
# sudo su -
# docker rm $(docker ps -a -q)
# docker rmi $(docker images -q -f dangling=true)