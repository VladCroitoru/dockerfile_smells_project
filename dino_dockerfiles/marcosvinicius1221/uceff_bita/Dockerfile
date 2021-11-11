From centos
RUN yum update -y
RUN yum install -y net-tool nano wget unzip java-1.8.0-openjdk
RUN yum clean all
RUN cd /root ; wget http://download.jboss.org/wildfly/10.1.0.Final/wildfly-10.1.0.Final.zip
RUN cd /root ; unzip wildfly-10.1.0.Final.zip
RUN cd /root ; mv wildfly-10.1.0.Final /opt/wildfly
RUN rm -Rf /root/
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]
EXPOSE 8080
