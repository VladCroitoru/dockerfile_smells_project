#jdk pre installed
FROM tomcat:8.5-jre8
MAINTAINER Wayner Barrios <waybarrios@gmail.com>

#
# Set GeoServer version and data directory 
#

ENV ROOT_TOMCAT="/usr/local/tomcat/webapps"\
    GEOSERVER_DATA_DIR="/geoserver_data"

#
# Download and install GeoServer
#
RUN cd $ROOT_TOMCAT
RUN wget -O geoserver.war https://googledrive.com/host/0B27czh8Ac9JqNWlQTHg5N3BmdUU 
#
# Extract geoserver.war
#
RUN unzip -q geoserver.war -d geoserver 
RUN rm geoserver.war
RUN mkdir $GEOSERVER_DATA_DIR
#
#Useful for import data into this folder 
#
VOLUME $GEOSERVER_DATA_DIR
