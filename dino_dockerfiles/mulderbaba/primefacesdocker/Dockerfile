FROM ubuntu:14.04

MAINTAINER Mert Caliskan <mcaliskan@gmail.com>

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install openjdk-7-jre-headless curl
RUN mkdir -p /usr/share/tomcat
RUN curl http://ftp.mku.edu.tr/apache-dist/tomcat/tomcat-8/v8.0.20/bin/apache-tomcat-8.0.20.tar.gz | tar zxf - --strip=1 -C /usr/share/tomcat/

RUN sudo apt-get install wget
RUN wget http://repository.primefaces.org/org/primefaces/showcase/5.2/showcase-5.2.war -P /usr/share/tomcat/webapps

CMD ["/usr/bin/java","-Djava.util.logging.config.file=/usr/share/tomcat/conf/logging.properties","-Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager","-Djava.endorsed.dirs=/usr/share/tomcat/endorsed","-classpath","/usr/share/tomcat/bin/bootstrap.jar:/usr/share/tomcat/bin/tomcat-juli.jar","-Dcatalina.base=/usr/share/tomcat","-Dcatalina.home=/usr/share/tomcat","-Djava.io.tmpdir=/usr/share/tomcat/temp","org.apache.catalina.startup.Bootstrap","start"]

EXPOSE 8080

