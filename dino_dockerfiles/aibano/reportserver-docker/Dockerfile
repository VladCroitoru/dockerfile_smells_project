#
# ReportServer
#

FROM aibano/tomcat-docker
MAINTAINER Osama Alaiban, megdam@gmail.com

# Create a directory in the tomcat webapps for the reportserver
RUN mkdir /usr/local/tomcat/webapps/reportserver

# Copy the environment file from host to container. 
ADD setenv.sh /usr/local/tomcat/bin

# Copy the report server zip file
RUN wget -P /usr/local/tomcat/webapps/reportserver/ https://github.com/aibano/reportserver-docker/raw/master/RS3.0.2-5855-2016-05-29-17-55-24-reportserver-ce.zip

RUN apt-get update && \
    apt-get install -y zip && \
    unzip /usr/local/tomcat/webapps/reportserver/RS3.0.2-5855-2016-05-29-17-55-24-reportserver-ce.zip -d /usr/local/tomcat/webapps/reportserver



# Copy database connection configuration file from host to container
ADD persistence.properties /usr/local/tomcat/webapps/reportserver/WEB-INF/classes/
