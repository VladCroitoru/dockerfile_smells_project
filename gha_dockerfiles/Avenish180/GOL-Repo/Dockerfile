FROM tomcat:8.0
MAINTAINER sankar
ARG CONT_IMG_VER
WORKDIR /usr/local/tomcat
EXPOSE 8080
COPY  ./gameoflife-web/target/gameoflife.war /usr/local/tomcat/webapps
