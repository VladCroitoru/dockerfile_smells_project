FROM ubuntu
RUN apt-get update
RUN apt-get install -y git-core
RUN apt-get install -y maven
RUN apt-get install -y openjdk-8-jdk
RUN mkdir /Repo
ADD Repo/pom.xml /Repo/pom.xml
ADD Repo/src /Repo/src
EXPOSE 8080
RUN mkdir /data
WORKDIR /Repo
CMD mvn jetty:run
	
