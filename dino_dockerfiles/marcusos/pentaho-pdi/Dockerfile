FROM phusion/baseimage:latest
MAINTAINER Marcus Oliveira da Silva <marcus.oli.silva@gmail.com>

#Base reference http://diethardsteiner.github.io/pdi/2016/04/21/PDI-Docker-Part-1.html

# Set correct environment variables.
ENV HOME /root
ENV PENTAHO_HOME /opt/pentaho
ENV PDI_HOME ${PENTAHO_HOME}/data-integration
ENV BASE_REL 7.0
ENV REV 0.0-25
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV MYSQL_JDBC_V mysql-connector-java-5.1.41

# =============================== Start Image Customization ===================
# Make sure base image is updated then install needed linux tools
RUN  apt-get update && \
     apt-get upgrade -f -y && \
     apt-get install -f -y wget curl git zip  

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer

# =============================== Installing PDI ===================
# ADD http://sourceforge.net/projects/pentaho/files/Data%20Integration/7.0/pdi-ce-7.0.0.0-25.zip/download 
RUN  mkdir /opt/pentaho/ && \
	 wget http://sourceforge.net/projects/pentaho/files/Data%20Integration/${BASE_REL}/pdi-ce-${BASE_REL}.${REV}.zip/download -O /opt/pentaho/pdi-ce.zip

RUN  unzip -q /opt/pentaho/pdi-ce.zip -d /opt/pentaho/ && \
     rm /opt/pentaho/pdi-ce.zip
RUN chmod +x /opt/pentaho/data-integration/carte.sh

# =============================== Installing JDBC drivers ===================
RUN mkdir /downloads && \
	wget https://dev.mysql.com/get/Downloads/Connector-J/${MYSQL_JDBC_V}.zip -O /downloads/mysql_jdbc.zip && \
	unzip -q /downloads/mysql_jdbc.zip -d /downloads/ && \
	cp /downloads/${MYSQL_JDBC_V}/${MYSQL_JDBC_V}-bin.jar /opt/pentaho/data-integration/lib/${MYSQL_JDBC_V}-bin.jar && \
    rm -rf /downloads/

# =============================== START ===================
# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


EXPOSE 8080
ADD configuration.xml /opt/pentaho/data-integration/configuration.xml

# Configure TimeZone (Set your locale).
RUN sed -i 's/ZONE=.*/ZONE=Brazil\/East/g' /etc/localtime && \
ln -sf /usr/share/zoneinfo/Brazil/East /etc/localtime
ENV PENTAHO_DI_JAVA_OPTIONS "-Xms1024m -Xmx2048m -XX:MaxPermSize=256m -Duser.timezone=Brazil/East"

CMD (/opt/pentaho/data-integration/carte.sh /opt/pentaho/data-integration/configuration.xml)

