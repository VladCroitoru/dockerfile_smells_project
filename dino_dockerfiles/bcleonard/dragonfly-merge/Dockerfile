FROM centos:7.1.1503
MAINTAINER Bradley Leonard <bradley@stygianresearch.com> 

# install java, mysql-connector-java, tomcat, unzip, wget
#RUN yum -y update\
# && yum -y install java-1.8.0-openjdk mysql-connector-java tomcat tomcat-webapps unzip wget\
RUN yum -y install java-1.8.0-openjdk mysql-connector-java tomcat tomcat-webapps unzip wget\
 && yum clean all

# link the mysql-connector-java.jar file
RUN ln -s /usr/share/java/mysql-connector-java.jar /usr/share/java/tomcat

EXPOSE 8080

#
# download and unzip the dragonfly code
#
RUN rm -rf -- /usr/share/tomcat/webapps/* &&\
  cd /usr/share/tomcat/webapps &&\
  wget https://github.com/FlatBallFlyer/IBM-Data-Merge-Utility/releases/download/v3.1.4/idmu-war-full-3.1.4if1.war -O ROOT.war &&\
  chown tomcat.tomcat ROOT.war

ADD run.sh /tmp/run.sh
RUN chmod 755 /tmp/run.sh

CMD ["/tmp/run.sh"]
