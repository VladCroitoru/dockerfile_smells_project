FROM ubuntu:trusty
MAINTAINER Jimmy Mesta <@jimmesta>

RUN apt-get update && apt-get install -y openjdk-7-jdk wget

# Install Dockerize

RUN wget https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-amd64-v0.2.0.tar.gz
RUN tar -C /usr/local/bin -xvzf dockerize-linux-amd64-v0.2.0.tar.gz

# Install Threadfix

RUN mkdir Threadfix
COPY Install /Threadfix

# Extract the war to add proper configs

WORKDIR /Threadfix/tomcat/webapps
RUN wget https://storage.googleapis.com/threadfix/threadfix.war
RUN mkdir /Threadfix/tomcat/webapps/threadfix 
WORKDIR /Threadfix/tomcat/webapps/threadfix 
RUN jar -xvf /Threadfix/tomcat/webapps/threadfix.war
COPY Install/jdbc.properties.tmpl /Threadfix/tomcat/webapps/threadfix/WEB-INF/classes/

WORKDIR /Threadfix
RUN chmod +x threadfix.sh
EXPOSE 8443
CMD ["/usr/local/bin/dockerize", "-template", "/Threadfix/tomcat/webapps/threadfix/WEB-INF/classes/jdbc.properties.tmpl:/Threadfix/tomcat/webapps/threadfix/WEB-INF/classes/jdbc.properties", "/Threadfix/threadfix.sh", "start"]

