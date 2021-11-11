FROM davidcaste/alpine-tomcat:tomcat8
MAINTAINER "Reboot Shen<reboot.shen@gmail.com>"
ADD tomcat-users.xml /opt/tomcat/conf/
ADD manager /opt/tomcat/webapps/manager
CMD ["/opt/tomcat/bin/catalina.sh", "run"]
