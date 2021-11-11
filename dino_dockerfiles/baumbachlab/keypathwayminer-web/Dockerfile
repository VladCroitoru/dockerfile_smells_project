FROM mlist/grails:2.5.6
MAINTAINER Markus List <markus.list@wzw.tum.de>

# Create App Directory
COPY . /app
WORKDIR /app

# Setup Grails paths
ENV GRAILS_HOME /usr/lib/jvm/grails
ENV PATH $GRAILS_HOME/bin:$PATH

# Setup Java paths
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV PATH $JAVA_HOME/bin:$PATH

# Compile kpm core and grails app
RUN cd keypathwayminer-core/ && \
apt-get update && \
apt-get install -y maven && \
mvn install && \ 
cd .. && \
grails refresh-dependencies && \ 
grails compile && \
grails prod war

RUN curl -O http://archive.apache.org/dist/tomcat/tomcat-7/v7.0.55/bin/apache-tomcat-7.0.55.tar.gz
RUN tar xzf apache-tomcat-7.0.55.tar.gz

CMD mv target/keypathwayminer.war apache-tomcat-7.0.55/webapps/

CMD apache-tomcat-7.0.55/bin/startup.sh && tail -f apache-tomcat-7.0.55/logs/catalina.out

# Expose port to outside world
EXPOSE 8080
