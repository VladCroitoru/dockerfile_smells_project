FROM ubuntu
MAINTAINER hobbyqhd “liubingxin1030@outlook.com”
ENV REFRESHED_AT 2017_06_14

RUN apt-get -yqq update
RUN apt-get -yqq install tomcat7 default-jdk
 
ENV CATALINA_HOME /usr/share/tomcat7
ENV CATALINA_BASE /var/lib/tomcat7
ENV CATALINA_PID /var/run/tomcat7.pid
ENV CATALINA_SH /usr/share/tomcat7/bin/catalina.sh
ENV CATALINA_TMPDIR /tmp/tomcat7-tomcat7-tmp
 
RUN mkdir -p $CATALINA_TMPDIR
 
VOLUME ["/var/lib/tomcat7/webapps/"]
 
EXPOSE 8080
 
ENTRYPOINT ["/usr/share/tomcat7/bin/catalina.sh", "run"]
