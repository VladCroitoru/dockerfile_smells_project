FROM ubuntu:trusty
MAINTAINER Jimmy Mesta <@jimmesta>

RUN apt-get update && apt-get install -y openjdk-7-jdk wget
RUN mkdir Threadfix 
COPY Install /Threadfix
WORKDIR /Threadfix/tomcat/webapps
RUN wget https://storage.googleapis.com/threadfix/threadfix.war
EXPOSE 8443
WORKDIR /Threadfix
RUN chmod +x threadfix.sh
ENTRYPOINT ["./threadfix.sh"]
