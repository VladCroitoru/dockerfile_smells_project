FROM tomcat:latest

#EXPOSE 7070

RUN apt-get update

RUN apt-get install maven -y

WORKDIR /root

ADD TomcatMavenApp TomcatMavenApp

WORKDIR TomcatMavenApp

RUN mvn clean install

RUN mvn package

RUN cp target/*.war /usr/local/tomcat/webapps.dist

RUN rm -rf /usr/local/tomcat/webapps/

RUN mv /usr/local/tomcat/webapps.dist /usr/local/tomcat/webapps

