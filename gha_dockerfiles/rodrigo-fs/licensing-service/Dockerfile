#TODO: Create file for debug and prod
FROM maven:3.8.2-jdk-11
#COPY . /project
#RUN cd /project && mvn package
RUN mkdir /app
WORKDIR /app
ADD /target/licensing-service-0.0.1-SNAPSHOT.jar ./
#ENTRYPOINT ["java","-jar","./licensing-service-0.0.1-SNAPSHOT.jar"]
#"-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=8080","-Djava.security.egd=file:/dev/./urandom"
#java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=8081 -Djava.security.egd=file:/dev/./urandom -jar /project/target/licensing-service-0.0.1-SNAPSHOT.jar
