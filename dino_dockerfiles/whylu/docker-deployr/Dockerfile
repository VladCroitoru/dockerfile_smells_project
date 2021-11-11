From centos:6.6

ENV RRO_VERSION=3.2.2
#el6 for centos6
#see: https://mran.revolutionanalytics.com/archives/
ENV OS_VERSION=el6
ENV MKL_VERSION=3.2.2
ENV RSERVER_VERSION=7.4.2
ENV DEPLOYR_VERSION=8.0.0


#install jdk1.7
ADD ./install_jdk1.7.sh /tmp/install_jdk1.7.sh 
RUN chmod +x /tmp/install_jdk1.7.sh \
    && source /tmp/install_jdk1.7.sh
ENV JAVA_HOME=/usr/lib/jvm/jdk1.7.0_79

#install prerequistes for deployr
ADD ./prerequisites.sh /tmp/prerequisites.sh
RUN chmod +x /tmp/prerequisites.sh \
    && source /tmp/prerequisites.sh

#install deployr
ADD ./install_deployr.sh /tmp/install_deployr.sh
RUN chmod +x /tmp/install_deployr.sh \
    && source /tmp/install_deployr.sh
ENV DEPLOYR_HOME=/opt/deployr/${DEPLOYR_VERSION}


# EXPOSE PORTS
# http://deployr.revolutionanalytics.com/documents/admin/install/#update-firewall
#Tomcat default port
EXPOSE 8000
#Tomcat HTTPS port
EXPOSE 8001
#DeployR event console port
EXPOSE 8006
#MongoDB port
EXPOSE 8003

RUN usermod -a -G root apache

ADD ./setExposeIpPort.sh /opt/setExposeIpPort.sh
RUN chmod +x /opt/setExposeIpPort.sh

ADD ./startDeployR.sh /opt/startDeployR.sh
RUN chmod +x /opt/startDeployR.sh
CMD /bin/bash -c "/opt/startDeployR.sh"

