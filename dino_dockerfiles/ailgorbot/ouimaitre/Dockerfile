#Download base image debian armhf
FROM armhf/debian

MAINTAINER AilgorBot <ailgorbot@gmail.com>

# Update Repositories
RUN apt-get update
RUN apt-get install -y wget
RUN wget http://archive.raspbian.org/raspbian.public.key -O - | apt-key add -
 
# Install dependencies
RUN apt-get install -y curl
RUN apt-get install -y unzip
RUN apt-get install -y build-essential
RUN apt-get install -y vim


# Install java8
RUN echo "deb http://archive.raspberrypi.org/debian/ jessie main" >> /etc/apt/sources.list.d/raspberrypi.list \
    && apt-get update \
    && apt-get install -y --force-yes oracle-java8-jdk \
    && ln -s /usr/lib/jvm/jdk-8-oracle-arm32-vfp-hflt /usr/lib/jvm/java-8-oracle


# Install tomcat9
RUN cd /opt  \
    && wget http://www.us.apache.org/dist/tomcat/tomcat-9/v9.0.0.M17/bin/apache-tomcat-9.0.0.M17.tar.gz  \
    && tar xzf apache-tomcat-9.0.0.M17.tar.gz  \
    && mv apache-tomcat-9.0.0.M17 tomcat9 \
    && rm apache-tomcat-9.0.0.M17.tar.gz


RUN echo 'export CATALINA_HOME='/opt/tomcat9'' >> /etc/environment
ENV CATALINA_HOME /opt/tomcat9

RUN echo 'export JAVA_HOME='/usr/lib/jvm/java-8-oracle'' >> /etc/environment
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN echo 'export JRE_HOME='/usr/lib/jvm/java-8-oracle/jre'' >> /etc/environment
ENV JRE_HOME /usr/lib/jvm/java-8-oracle/jre


ADD tomcat-users.xml /opt/tomcat9/conf/tomcat-users.xml
ADD context.xml /opt/tomcat9/webapps/manager/META-INF/context.xml


# standard clean operations
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#expose ports
EXPOSE 8080
EXPOSE 8009

# add volume for webapps folder
VOLUME /opt/tomcat9/webapps

#start tomcat
CMD bash
