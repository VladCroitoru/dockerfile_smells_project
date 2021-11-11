#dockerfile/emooti/emootidocker
# Setup Tomcat7 server
FROM ubuntu:14.04
MAINTAINER Uta Kapp "uta.kapp@emooti.org"
RUN apt-get update
RUN apt-get -y install curl vim git maven
RUN apt-get -y install openjdk-7-jre
#RUN apt-get -y install openjdk-7-jre openjdk-7-jdk
#RUN apt-get -y install tzdata tzdata-java tomcat7
# apt-get install tomcat7-docs tomcat7-admin tomcat7-examples
RUN apt-get -y install tomcat7 tomcat7-admin
RUN apt-get update
ENV CATALINA_HOME /usr/share/tomcat7
ENV CATALINA_BASE /var/lib/tomcat7
ENV CATALINA_PID /var/run/tomcat7.pid
ENV CATALINA_SH /usr/share/tomcat7/bin/catalina.sh
ENV CATALINA_TMPDIR /tmp/tomcat7-tomcat7-tmp
RUN mkdir -p $CATALINA_TMPDIR
VOLUME ["/var/lib/tomcat7/webapps/"]
# /var/lib/tomcat7 /etc/tomcat7 /usr/share/tomcat7 /usr/share/tomcat7/bin/startup.sh /usr/share/tomcat7/log
RUN mkdir -p /usr/share/tomcat7/logs
#bug in ap-get tomcat7
RUN cp -R /var/lib/tomcat7/common/ /usr/share/tomcat7/common/
RUN cp -R /var/lib/tomcat7/server/ /usr/share/tomcat7/server/
RUN cp -R /var/lib/tomcat7/shared/ /usr/share/tomcat7/shared/
RUN sed -i -- 's/<Context>/<Context reloadable="true">/g' /var/lib/tomcat7/conf/context.xml
EXPOSE 8080
#CMD ["/usr/share/tomcat7/bin/catalina.sh", "run"]
