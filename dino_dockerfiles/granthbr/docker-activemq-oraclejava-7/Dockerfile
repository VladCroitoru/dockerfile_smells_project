FROM      java
 
MAINTAINER Brandon Grantham <brandon.grantham@gmail.com>

RUN        apt-get update && \ 
           apt-get upgrade -y && \
           apt-get install -y python-software-properties && \
           apt-get install software-properties-common python-software-properties -y && \
           apt-get -y install curl telnet vim inetutils-ping 
WORKDIR    /opt

RUN 	   curl -LO http://apache.mirrors.ovh.net/ftp.apache.org/dist/activemq/5.14.0/apache-activemq-5.14.0-bin.tar.gz && \
           tar zxvf apache-activemq-5.14.0-bin.tar.gz && \
           ln -sf /opt/apache-activemq-5.14.0 /opt/activemq && \
           ln -sf /opt/activemq/bin/activemq /etc/init.d/ && \
           update-rc.d activemq defaults && \
           /etc/init.d/activemq setup /etc/default/activemq

# Use our own /etc/default/activemq to activate jmx
ADD etc/default /etc/default

# Use our own activemq.xml config
#ADD conf apache-activemq-5.10/conf
#VOLUME ["conf"]
#RUN chmod 600 activemq/conf/jmx.password

EXPOSE 6155 6156 61616 61617 1099 8161 61613

CMD java -Xmx1G -Dcom.sun.management.jmxremote.ssl=false \
-Dcom.sun.management.jmxremote.password.file=/opt/activemq/conf/jmx.password \
-Dcom.sun.management.jmxremote.access.file=/opt/activemq/conf/jmx.access \
-Djava.util.logging.config.file=logging.properties -Dcom.sun.management.jmxremote \
-Djava.io.tmpdir=/opt/activemq/tmp -Dactivemq.classpath=/opt/activemq/conf \
-Dactivemq.home=/opt/activemq -Dactivemq.base=/opt/activemq \
-Dactivemq.conf=/opt/activemq/conf \
-Dactivemq.data=/opt/activemq/data -jar /opt/activemq/bin/activemq.jar start
