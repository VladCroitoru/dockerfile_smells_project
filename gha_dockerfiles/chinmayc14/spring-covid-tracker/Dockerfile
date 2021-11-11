FROM openjdk:11
EXPOSE 8080
WORKDIR /

RUN apt-get update  
RUN apt-get install -y maven

ADD pom.xml /pom.xml  
RUN ["mvn", "dependency:resolve"]  
RUN ["mvn", "verify"]

ADD src /src  
RUN ["mvn", "package"]


ADD target/covid-tracker-0.0.1-SNAPSHOT.jar covid-tracker.jar 
ENTRYPOINT ["java","-jar","/covid-tracker.jar"]
