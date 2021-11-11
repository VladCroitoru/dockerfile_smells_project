# /*FROM centos:latest
# MAINTAINER sanjay.dahiya332@gmail.com
# RUN yum install -y httpd \
#   zip \
#  unzip 
# ADD https://www.free-css.com/assets/files/free-css-templates/download/page254/photogenic.zip /var/www/html/
# WORKDIR /var/www/html
# RUN unzip photogenic.zip
# RUN cp -rvf photogenic/* .
# RUN rm -rf photogenic photogenic.zip 
# CMD ["/usr/sbin/httpd", "-D",  "FOREGROUND"]
# EXPOSE 80


FROM maven:3.6.3-jdk-8-slim AS build
WORKDIR /home/app
COPY . /home/app
RUN mvn -f /home/app/pom.xml clean package

FROM openjdk:8-jdk-alpine
VOLUME /tmp
EXPOSE 5000
COPY --from=build /home/app/target/*.jar app.jar
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar /app.jar" ]
