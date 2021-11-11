FROM ubuntu:14.04

RUN apt-get update

RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:openjdk-r/ppa
RUN apt-get update
RUN apt-get install -y openjdk-8-jdk

ADD http://www-us.apache.org/dist/tomcat/tomcat-8/v8.0.39/bin/apache-tomcat-8.0.39.tar.gz /opt/apache-tomcat-8.0.39.tar.gz

RUN groupadd tomcat
RUN useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat

RUN mkdir /opt/tomcat
RUN tar xzvf /opt/apache-tomcat-8*tar.gz -C /opt/tomcat --strip-components=1
RUN cd /opt/tomcat
RUN chgrp -R tomcat /opt/tomcat
RUN chmod -R g+r conf
RUN chmod g+x conf
RUN chown -R tomcat webapps/ work/ temp/ logs/
