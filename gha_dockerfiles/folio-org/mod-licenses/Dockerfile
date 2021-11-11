FROM folioci/alpine-jre-openjdk11:latest
MAINTAINER Ian.Ibbotson@k-int.com
VOLUME /tmp
ENV VERTICLE_FILE mod-licenses.war
ENV VERTICLE_HOME /
COPY service/build/libs/mod-licenses-*.*.*.jar mod-licenses.war
EXPOSE 8080/tcp
