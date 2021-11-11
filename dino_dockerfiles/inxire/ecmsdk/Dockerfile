FROM ubuntu:14.04.1

MAINTAINER Frank Closheim <frank.closheim@inxire.com>

ADD chkconfig /sbin/chkconfig
ADD init.ora /
ADD initXETemp.ora /
ADD oracle-xe_11.2.0-1.0_amd64.debaa /
ADD oracle-xe_11.2.0-1.0_amd64.debab /
ADD oracle-xe_11.2.0-1.0_amd64.debac /
# ADD oracle-xe_11.2.0-1.0_amd64.deb /
RUN cat /oracle-xe_11.2.0-1.0_amd64.deba* > /oracle-xe_11.2.0-1.0_amd64.deb

# Install sshd
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:admin' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo "export VISIBLE=now" >> /etc/profile

# Prepare to install Oracle
RUN apt-get install -y libaio1 net-tools bc
RUN ln -s /usr/bin/awk /bin/awk
RUN mkdir /var/lock/subsys
RUN chmod 755 /sbin/chkconfig

# Install Oracle
RUN dpkg --install /oracle-xe_11.2.0-1.0_amd64.deb

RUN mv /init.ora /u01/app/oracle/product/11.2.0/xe/config/scripts
RUN mv /initXETemp.ora /u01/app/oracle/product/11.2.0/xe/config/scripts

RUN printf 8088\\n1521\\noracle\\noracle\\ny\\n | /etc/init.d/oracle-xe configure

RUN echo 'export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe' >> /etc/bash.bashrc
RUN echo 'export PATH=$ORACLE_HOME/bin:$PATH' >> /etc/bash.bashrc
RUN echo 'export ORACLE_SID=XE' >> /etc/bash.bashrc

ENV ORACLE_HOME /u01/app/oracle/product/11.2.0/xe
ENV ORACLE_SID XE

# Remove installation files
RUN rm /oracle-xe_11.2.0-1.0_amd64.deb*

EXPOSE 22
EXPOSE 1521
EXPOSE 8088

# Java Installation
RUN apt-get update
RUN apt-get -f install
RUN apt-get install -y openjdk-7-jre
RUN rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64
RUN chown -R oracle:dba ${JAVA_HOME}
RUN echo 'export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64' >> /etc/bash.bashrc

#Tomcat installation
ENV CATALINA_HOME /u01/app/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
RUN echo 'export CATALINA_HOME=/u01/app/tomcat' >> /etc/bash.bashrc; \
    echo 'export PATH=$CATALINA_HOME/bin:$PATH' >> /etc/bash.bashrc
RUN mkdir -p "$CATALINA_HOME"
ENV TOMCAT_MINOR_VERSION 8.0.20
RUN apt-get update
RUN apt-get install -y curl
RUN curl -O http://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_MINOR_VERSION}/bin/apache-tomcat-${TOMCAT_MINOR_VERSION}.tar.gz && \
 curl http://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_MINOR_VERSION}/bin/apache-tomcat-${TOMCAT_MINOR_VERSION}.tar.gz.md5 | md5sum -c - && \
 gunzip apache-tomcat-*.tar.gz && \
 tar xf apache-tomcat-*.tar && \
 mv apache-tomcat*/* ${CATALINA_HOME} && rm -Rf apache-tomcat-* \
 rm -rf ${CATALINA_HOME}/webapps/examples \
  ${CATALINA_HOME}/webapps/docs ${CATALINA_HOME}/webapps/ROOT \
  ${CATALINA_HOME}/webapps/host-manager \
  ${CATALINA_HOME}/RELEASE-NOTES ${CATALINA_HOME}/RUNNING.txt \
  ${CATALINA_HOME}/bin/*.bat ${CATALINA_HOME}/bin/*.tar.gz
RUN rm -rf /var/lib/apt/lists/*
ADD tomcat-users.xml context.xml $CATALINA_HOME/conf/

EXPOSE 8080

# ECMSDK Installation
ADD ecmsdk-xe.tar.gz /u01/app/oracle/product
RUN chown -R oracle:dba /u01/app/oracle/product/ecmsdk
RUN chmod u+x /u01/app/oracle/product/ecmsdk/bin/*.sh && \
    chmod u+x /u01/app/oracle/product/ecmsdk/install/*.sh
RUN echo 'export ECMSDK_HOME=/u01/app/oracle/product/ecmsdk' >> /etc/bash.bashrc
ENV ECMSDK_HOME /u01/app/oracle/product/ecmsdk
RUN cp $ECMSDK_HOME/lib/*.jar $CATALINA_HOME/lib/
RUN /u01/app/oracle/product/ecmsdk/install/init_repos.sh
COPY ecmsdk.war $CATALINA_HOME/webapps/

# Command that is used during container startup
CMD	sed -i -E "s/HOST = [^)]+/HOST = $HOSTNAME/g" /u01/app/oracle/product/11.2.0/xe/network/admin/listener.ora; \
    sed -i -E "s/HOST = [^)]+/HOST = $HOSTNAME/g" /u01/app/oracle/product/11.2.0/xe/network/admin/tnsnames.ora; \
    su -m oracle -c '/u01/app/oracle/product/11.2.0/xe/bin/lsnrctl start'; \
    service oracle-xe start; \
    startup.sh; \
	  /usr/sbin/sshd -D