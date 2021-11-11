FROM maven:3-jdk-8-alpine
MAINTAINER siva chedde (cheddesi@gmail.com)
ENV REFRESHED_AT 2018-04-04

#install git and openssh
RUN apk update && apk upgrade && \
    apk add --no-cache git openssh
#create hippo directory
RUN cd /usr/share && mkdir hippo
#clone the git repo
RUN cd /usr/share/hippo && git clone -b develop https://github.com/cheddesi/camel-events-support.git
#add ca certs
ADD certs /usr/share/
#import elasticsearch ca cert
RUN keytool -importcert -noprompt -trustcacerts -file /usr/share/ca/ca.crt -keystore /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/cacerts -storepass changeit
#run mvn clean
RUN cd /usr/share/hippo/camel-events-support/demo && mvn clean verify
#expose port 8080 of tomcat
EXPOSE 8080
#Right directory
WORKDIR /usr/share/hippo/camel-events-support/demo
#Entry point for container
CMD mvn -Pcargo.run
