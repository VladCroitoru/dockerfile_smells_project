FROM platformer/tomcat7
MAINTAINER Dorde Cvijanovic <cdorde@gmail.com>

RUN apt-get -qq update
RUN apt-get -qqy install unzip

ADD jasper_6.2.0-start.sh /usr/local/bin/jasper_6.2.0-start.sh
ADD install_jasper_6.2.0.sh /usr/local/bin/install_jasper_6.2.0.sh
RUN chmod +x /usr/local/bin/jasper_6.2.0-start.sh
RUN chmod +x /usr/local/bin/install_jasper_6.2.0.sh

#Add JDBC
RUN apt-get -qqy install wget
RUN wget "http://www.java2s.com/Code/JarDownload/ojdbc6/ojdbc6.jar.zip" -P /tmp -O /tmp/ojdbc6.jar.zip
RUN unzip /tmp/ojdbc6.jar.zip -d /tmp
RUN cp /tmp/ojdbc6.jar /usr/share/tomcat7/lib
RUN rm /tmp/ojdbc6.jar.zip
RUN rm /tmp/ojdbc6.jar

WORKDIR /tmp
#ADD jasperreports-server-cp-6.2.0-bin.zip /tmp/jasperreports-server-cp-6.2.0-bin.zip
RUN wget -nv "http://downloads.sourceforge.net/project/jasperserver/JasperServer/JasperReports%20Server%20Community%20Edition%206.2.0/jasperreports-server-cp-6.2.0-bin.zip?r=http%3A%2F%2Fcommunity.jaspersoft.com%2Fproject%2Fjasperreports-server%2Freleases&ts=1455349225&use_mirror=netcologne" -P /tmp -O /tmp/jasperreports-server-cp-6.2.0-bin.zip
RUN unzip /tmp/jasperreports-server-cp-6.2.0-bin.zip
RUN /bin/rm /tmp/jasperreports-server-cp-6.2.0-bin.zip
ADD default_master.properties /tmp/jasperreports-server-cp-6.2.0-bin/buildomatic/default_master.properties

CMD ["/usr/local/bin/jasper_6.2.0-start.sh"]

EXPOSE 8080
