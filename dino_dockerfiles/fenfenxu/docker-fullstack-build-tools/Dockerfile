# DOCKER-VERSION 0.7.1
FROM      ubuntu:14.04
MAINTAINER liuxu <liuluxu1989@126.com>


# install ruby
RUN apt-get -y update
RUN apt-get -y install make build-essential zlib1g-dev libssl-dev libreadline6-dev libyaml-dev wget tar
RUN cd /tmp \
  && wget http://cache.ruby-lang.org/pub/ruby/2.0/ruby-2.0.0-p481.tar.gz \
  && tar -xvzf ruby-2.0.0-p481.tar.gz \
  && cd ruby-2.0.0-p481/ \
  && ./configure --prefix=/usr/local \
  && make \
  && make install

  

# install compass
RUN gem install --no-rdoc --no-ri compass

# make sure the package repository is up to date
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN apt-get -y update

# install python-software-properties、ssh (so you can do add-apt-repository)
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-software-properties \
  software-properties-common\
  openssh-server \
  && mkdir /var/run/sshd


# install oracle java from PPA
RUN add-apt-repository ppa:webupd8team/java -y
RUN apt-get update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get -y install oracle-java8-installer && apt-get clean

# Set oracle java as the default java
RUN update-java-alternatives -s java-8-oracle
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc

# install utilities, maven
RUN apt-get -y install vim git sudo zip bzip2 fontconfig curl mc maven

# install node.js from PPA
RUN add-apt-repository ppa:chris-lea/node.js
RUN apt-get update
RUN apt-get -y install nodejs


# install yeoman, JHipster, angular and express
RUN npm install -g yo \
  grunt-cli \
  gulp \
  bower \
  generator-jhipster@1.10.1 \
  generator-angular \
  express-generator \
  http-server \
  n
RUN n stable

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
