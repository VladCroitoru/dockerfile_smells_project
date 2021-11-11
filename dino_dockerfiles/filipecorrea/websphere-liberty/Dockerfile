FROM websphere-liberty:8.5.5
# Ubuntu 14.04.4 LTS
# IBM Java 1.8.0

ENV LICENSE accept

# Install Java Open JDK 7
RUN apt-get update && apt-get install -y openjdk-7-jdk

# Setup paths to Java Open JDK 7
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/
ENV PATH $JAVA_HOME/bin:$PATH

# Install Apache Maven
RUN apt-get install -y maven

# Change work directory to /tmp
WORKDIR /tmp

# Add pom.xml
ADD pom.xml /tmp/pom.xml

# Get all the downloads out of the way
RUN mvn verify clean --fail-never

# Add source folder
ADD src /tmp/src

# Compile and package application
RUN mvn verify

# Copy generated WAR file to server
RUN cp /tmp/target/Sample.war /opt/ibm/wlp/usr/servers/defaultServer/dropins/
