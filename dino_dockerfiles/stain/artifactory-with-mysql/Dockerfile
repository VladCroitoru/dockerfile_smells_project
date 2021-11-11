FROM mattgruter/artifactory

MAINTAINER Stian Soiland-Reyes <soiland-reyes@cs.manchester.ac.uk>


# Configure to use mysql 
# https://www.jfrog.com/confluence/display/RTF/MySQL
 
ADD http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.35/mysql-connector-java-5.1.35.jar /usr/local/tomcat/lib/

ADD http://subversion.jfrog.org/artifactory/public/trunk/distribution/standalone/src/main/install/misc/db/mysql.properties /artifactory/etc/storage.properties
# but change localhost to mysql for mySQL container --link
RUN sed -i s/localhost/mysql/ /artifactory/etc/storage.properties

# In case the above mysql.properties becomes unavailable:
#ADD mysql.properties /artifactory/etc/storage.properties


# Expose Artifactories data, log and backup directory.
VOLUME /artifactory/data
VOLUME /artifactory/logs
VOLUME /artifactory/backup

WORKDIR /artifactory
