FROM ubuntu:14.04

MAINTAINER lucy "lucy.derlin@gmail.com"

RUN apt-get update && apt-get install -y wget unzip expect pwgen && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/oracle && \
    wget -q --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2Ftechnetwork%2Fjava%2Fjavase%2Fdownloads%2Fjdk7-downloads-1880260.html; oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/7u60-b19/jdk-7u60-linux-x64.tar.gz && \
    mv -v  jdk-7u60-linux-x64.tar.gz /opt/oracle && \ 
    cd /opt/oracle && tar zxf jdk-7u60-linux-x64.tar.gz && \
    cd /opt/oracle/ && rm -vf jdk-7u60-linux-x64.tar.gz  && \
    ln -svn /opt/oracle/jdk1.7.0_60 /opt/oracle/jdk && \
    echo "JAVA_HOME=/opt/oracle/jdk" >> /etc/environment

ENV JAVA_HOME /opt/oracle/jdk
ENV PATH $JAVA_HOME/bin:$PATH

RUN wget -q  --no-cookies --no-check http://download.java.net/glassfish/4.1/release/glassfish-4.1.zip && \
    mv -v glassfish-4.1.zip /opt/oracle/ && \
    cd /opt/oracle && unzip -q glassfish-4.1.zip && \
    ln -svn /opt/oracle/glassfish4 /opt/oracle/glassfish && \
    rm -f /opt/oracle/glassfish-4.1.zip && \
    echo "GLASSFISH_HOME=/opt/oracle/glassfish"

ENV GLASSFISH_HOME /opt/oracle/glassfish
ENV PATH $GLASSFISH_HOME/bin:$PATH

ADD run.sh /run.sh
ADD change_admin_pass.expect /change_admin_pass.expect
ADD asadmin_cmd.expect /asadmin_cmd.expect

RUN chmod +x run.sh && \
    chmod +x *.expect

# 4848 (administration), 8080 (HTTP listener), 8181 (HTTPS listener)
EXPOSE 4848 8080 8181 1527

CMD ["/run.sh"]

ENV DERBY_HOME /opt/oracle/glassfish4/javadb/bin/

#ADD WeddingSiteApp.war /opt/oracle/glassfish4/glassfish/domains/domain1/autodeploy/

#RUN ["/run.sh"]
