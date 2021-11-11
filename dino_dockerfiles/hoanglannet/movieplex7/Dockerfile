FROM ubuntu:14.04
MAINTAINER Lan Le <hoanglannet@gmail.com>

# install jdk wget maven git
RUN apt-get install -y openjdk-7-jdk wget
RUN apt-get install -y maven git

# setup Wildfly
RUN wget -O /opt/wildfly-9.0.2.Final.tar.gz http://download.jboss.org/wildfly/9.0.2.Final/wildfly-9.0.2.Final.tar.gz
RUN (cd /opt && tar zxf /opt/wildfly-9.0.2.Final.tar.gz)
RUN (mv /opt/wildfly-* /opt/wildfly)

# setup Java
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64

# install app
RUN (git clone https://github.com/hoanglannet/movieplex7.git)
RUN  (mkdir movieplex7)
RUN (cd movieplex7 &&  git pull origin master && mvn clean package)
RUN (cp /movieplex7/target/*.war /opt/wildfly/standalone/deployments/)

# expose the ports we are interested in
EXPOSE 8080 9990

# add user for management wildfly
RUN /opt/wildfly/bin/add-user.sh admin Admin

# set the default command to run on boot
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
