###########################
# Install FROM UBUNTU IMAGE
FROM ubuntu:16.04

# Author
MAINTAINER AlexT

# RUN COMMAND BASICALLY runs the command in the terminal and creates an image.
# Install all the updates for UBUNTU
RUN apt-get update && apt-get install -y python-software-properties software-properties-common

# Install all the updates for UBUNTU
RUN apt-get install -y iputils-ping

#Open JDK
RUN apt-get install -y openjdk-8-jdk

RUN apt-get install -y maven

# ADD a directory called docker-demo-image inside the UBUNTU IMAGE where you will be moving all of these files under this
# DIRECTORY to
ADD . /usr/local/docker-demo-image

# AFTER YOU HAVE MOVED ALL THE FILES GO AHEAD CD into the directory and run mvn assembly.
# Maven assembly will package the project into a JAR FILE which can be executed
RUN cd /usr/local/docker-demo-image && mvn install -DskipTests

#THE CMD COMMAND tells docker the command to run when the container is started up from the image. In this case we are
# executing the java program as is to print Hello World.
CMD ["java", "-jar", "/usr/local/docker-demo-image/target/image-0.0.1-SNAPSHOT.jar"]
##