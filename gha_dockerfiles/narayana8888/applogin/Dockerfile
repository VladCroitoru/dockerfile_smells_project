FROM ubuntu
MAINTAINER tejesh
RUN apt-get -y update && apt-get -y upgrade && \
apt-get -y install openjdk-8-jdk wget && \
mkdir /usr/local/tomcat
RUN wget https://downloads.apache.org/tomcat/tomcat-9/v9.0.52/bin/apache-tomcat-9.0.52.tar.gz  -O /tmp/tomcat.tar.gz
RUN cd /tmp && tar xvfz tomcat.tar.gz && cp -Rv /tmp/apache-tomcat-9.0.52/* /usr/local/tomcat/
ADD https://github.com/tejesh555/applogin/raw/master/target/applogin-1.0.war /usr/local/tomcat/webapps/applogin
EXPOSE 8080
CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]

# build the image:  docker build -t applogin .
# run the image : docker run --name applogin -d -p 8080:8080 applogin
# access it by : <ip>:8080/applogin
