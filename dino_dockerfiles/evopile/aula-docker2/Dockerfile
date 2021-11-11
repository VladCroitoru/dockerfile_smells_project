FROM centos:centos7.3.1611

MAINTAINER Everton <evopileco@hotmail.com>
RUN yum update -y && yum -y install xmlstarlet saxon augeas bsdtar unzip deltarpm java-1.8.0-openjdk wget && yum clean all

RUN groupadd -r wildfly -g 1000 && useradd -u 1000 -r -g wildfly -m -d /opt/wildfly -s /sbin/nologin -c "wildfly user" wildfly

RUN cd /opt 
RUN wget http://download.jboss.org/wildfly/10.1.0.Final/wildfly-10.1.0.Final.tar.gz
RUN tar -zxvf wildfly-10.1.0.Final.tar.gz
RUN mv wildfly-10.1.0.Final /opt/wildfly

RUN rm -r -f /opt/wildfly-10.1.0.Final.tar.gz

RUN chmod 755 /opt/wildfly

WORKDIR /opt/wildfly

CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]

EXPOSE 8080

USER wildfly
