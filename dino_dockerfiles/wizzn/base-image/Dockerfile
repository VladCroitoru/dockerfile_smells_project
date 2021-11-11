FROM debian:jessie-backports
MAINTAINER Martin Verspai martin.verspai@iteratec.de

EXPOSE 8080 9990

# Create deploy directories
RUN mkdir -p /opt/oracle
RUN mkdir -p /opt/jboss
RUN mkdir -p /var/log/wildfly
RUN mkdir -p /opt/shared

# Download and configure required software
RUN apt-get update && apt-get -y install wget
RUN wget --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u51-b16/jdk-8u51-linux-x64.tar.gz
RUN wget http://download.jboss.org/wildfly/9.0.1.Final/wildfly-9.0.1.Final.tar.gz

RUN tar -zxf jdk-8u51-linux-x64.tar.gz -C /opt/oracle
RUN tar -zxf wildfly-9.0.1.Final.tar.gz -C /opt/jboss

RUN ln -s /opt/oracle/jdk1.8.0_51 /opt/oracle/jdk
RUN ln -s /opt/jboss/wildfly-9.0.1.Final /opt/jboss/wildfly

RUN update-alternatives --install /usr/bin/java java /opt/oracle/jdk/bin/java 100

ADD sqljdbc41.jar /opt/jboss/wildfly/standalone/deployments/
ADD startup.sh /opt/jboss/startup.sh

# Cleaning up unused files
RUN rm jdk-8u51-linux-x64.tar.gz
RUN rm wildfly-9.0.1.Final.tar.gz
RUN apt-get -y remove wget
RUN apt-get -y autoremove
RUN apt-get clean

# Adding users for maintenance
RUN useradd -d /opt/jboss -s /bin/bash jboss

# Setting appropriate user permissions and deployabled
RUN chown -R jboss:jboss /opt/jboss
RUN chown -R jboss:jboss /opt/shared
RUN chown -R jboss:jboss /var/log/wildfly
RUN chmod g+w /opt/jboss/wildfly/standalone/deployments
RUN chmod u+x /opt/jboss/startup.sh

USER jboss

CMD /opt/jboss/startup.sh