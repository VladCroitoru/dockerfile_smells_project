FROM jboss/base-jdk:7

ENV JBOSS_HOME /opt/jboss/jboss-as-7.1.1.Final

# USER root

# RUN yum install -y openssh-server && \
#    mkdir /var/run/sshd && \
#    echo 'root:admin' | chpasswd && \
#    sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
#    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# USER jboss

COPY ojdbc7.jar /tmp

RUN cd $HOME \
 && curl -O http://download.jboss.org/jbossas/7.1/jboss-as-7.1.1.Final/jboss-as-7.1.1.Final.tar.gz \
 && tar xf jboss-as-7.1.1.Final.tar.gz \
 && rm jboss-as-7.1.1.Final.tar.gz     
       
# RUN /opt/jboss/jboss-as-7.1.1.Final/bin/add-user.sh --silent=true admin admin   

# RUN /opt/jboss/jboss-as-7.1.1.Final/bin/jboss-cli.sh --command="module add --name=com.oracle.jdbc --resources=/tmp/ojdbc7.jar --dependencies=javax.api,javax.transaction.api" && \
#    /opt/jboss/jboss-as-7.1.1.Final/bin/jboss-cli.sh --commands=embed-server,/subsystem=datasources/jdbc-driver=oracle:add\(driver-name=ojbdc7,driver-module-name=com.oracle.jdbc,driver-xa-datasource-class-name=oracle.jdbc.xa.client.OracleXADataSource\),stop-embedded-server 
    
ENV LAUNCH_JBOSS_IN_BACKGROUND true
    
EXPOSE 8080 9990 
#22   

# ENTRYPOINT ["/usr/sbin/sshd","-D","&"]

CMD ["/opt/jboss/jboss-as-7.1.1.Final/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
