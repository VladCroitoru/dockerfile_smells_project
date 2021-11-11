FROM google/debian:wheezy
RUN apt-get update
RUN apt-get -y install curl
RUN apt-get install -y openjdk-7-jre
RUN apt-get install -y tomcat7
RUN curl -L http://sourceforge.net/projects/openmrs/files/releases/OpenMRS_Platform_1.10.1/openmrs.war/download -o /var/lib/tomcat7/webapps/openmrs.war
ADD openmrs-runtime.properties /var/lib/tomcat7/openmrs-runtime.properties
RUN apt-get install -y mysql-server
ADD run.sh /root/run.sh
RUN chmod +x /root/run.sh
EXPOSE 8080
CMD ["/root/run.sh"]