# NTIPA-Jbilling-Docker
FROM tornabene/docker-ntipa-base

MAINTAINER Giambanco Giuseppe <giambancogiuseppe@yahoo.it>

RUN apt-get -y install vim git zip unzip bzip2
RUN apt-get -y install sudo wget


# mi posiziono sul contesto della cartella opt
WORKDIR /opt
# Download jbilling
RUN wget http://cznic.dl.sourceforge.net/project/jbilling/jbilling%20Latest%20Stable/jbilling-3.1.0/jbilling-community-3.1.0.zip -O jbilling-community-3.1.0.zip
# qui scompatterò il file da scaricare (link da verificare )
RUN unzip jbilling-community-3.1.0.zip
#Privilegi per installare jbilling




#WORKDIR /opt/jbilling-community-3.1.0/lib
#RUN wget http://central.maven.org/maven2/org/postgresql/postgresql/9.3-1100-jdbc41/postgresql-9.3-1100-jdbc41.jar
#RUN wget http://central.maven.org/maven2/org/hsqldb/hsqldb/2.2.8/hsqldb-2.2.8.jar
#sudo mkdir -p /home/jbilling/jbilling/enterprise/image/bin/hsql/
#sudo chmod 777  /home/jbilling/
#sudo  chmod -R 777  /home/jbilling/
#ADD jbilling-DataSource.groovy /opt/jbilling-community-3.1.0/jbilling/jbilling-DataSource.groovy


WORKDIR /opt/jbilling-community-3.1.0/bin
#Allego supervisor
ADD jbilling.sh /opt/jbilling-community-3.1.0/bin/jbilling.sh
ADD jbilling.conf  /etc/supervisor/conf.d/jbilling.conf
RUN chmod +x *.sh


EXPOSE 8080

CMD /usr/bin/supervisord