  
FROM ubuntu:latest
ENV TOMCAT_VERSION=8.5.50

# to skip the eographic area:
ENV DEBIAN_FRONTEND=nonintercative 
RUN apt-get update &&  apt-get upgrade -y &&\
    apt-get install -y apt-file && \
    apt-file update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y wget && \
    apt-get install -y maven && \
    apt-get install -y git && \
    apt-get clean;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# Setup JAVA_HOME -- useful for docker commandline
ENV M2_HOME /usr/share/maven/
RUN export M2_HOME


#Install tomcat8
RUN wget --quiet --no-cookies https://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/tomcat.tar.gz

RUN cd /tmp && tar xvfz tomcat.tar.gz
RUN mkdir -pv /usr/local/tomcat
CMD [ "chmod ugo+rwx /usr/local/tomcat/" ]
#RUN cd /usr/local/tomcat/
RUN cp -Rf /tmp/apache-tomcat-8.5.50/* /usr/local/tomcat/

#PORT EXPOSE
EXPOSE 8080
WORKDIR /var/lib/jenkins/workspace/SONAR-QUBE-jenkins-pipeline/target/
#RUN cp -Rf /var/lib/jenkins/workspace/SONAR-QUBE-jenkins-pipeline/target/*.war /usr/local/tomcat/webapps/app.war
COPY ./target/*.war /usr/local/tomcat/webapps/app.war 

RUN cd /usr/local/tomcat/conf
RUN sed -i '/<\/tomcat-users>/ i\  <user username="tomcat" password="tomcat" roles="manager-gui"/>' /usr/local/tomcat/conf/tomcat-users.xml
RUN cd /usr/local/tomcat/bin && \
    ./shutdown.sh && \
    ./startup.sh;

CMD ["/usr/local/tomcat/bin/catalina.sh", "run" ]
