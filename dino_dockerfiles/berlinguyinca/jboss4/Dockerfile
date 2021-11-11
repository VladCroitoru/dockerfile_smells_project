FROM openjdk:7 
MAINTAINER Martin Callesen <martin.callesen@gmail.com>, Gert Wohlgemuth <wohlgemuth@ucdavis.edu>
RUN useradd -m -d /opt/jboss -s /bin/bash jboss
USER jboss
RUN cd $home && wget http://sourceforge.net/projects/jboss/files/JBoss/JBoss-4.2.3.GA/jboss-4.2.3.GA.zip && unzip jboss-4.2.3.GA.zip && rm jboss-4.2.3.GA.zip

# Enable remote debugging 
ENV JAVA_OPTS=-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=8000

# Expose the ports we're interested in
# Webserver is running on 8080 
# Adminserver is running on 9990
# Remote debug port can be accessed on 8000
EXPOSE 8080 9990 8000 1098 1099 3873 4444 4445 4446 8009 8083 8090 8092 8093

# Configurations
ENV JBOSS_HOME=/opt/jboss/jboss-4.2.3.GA
ADD ejb3/jboss-service.xml /opt/jboss/jboss-4.2.3.GA/server/default/deploy/ejb3.deployer/META-INF/jboss-service.xml

ADD run.sh /opt/run.sh
# Set the default command to run on boot
CMD ["/bin/bash", "/opt/run.sh"]
