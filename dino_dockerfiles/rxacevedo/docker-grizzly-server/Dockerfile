FROM maven:latest
MAINTAINER rxacevedo@fastmail.com

RUN mvn archetype:generate -DarchetypeArtifactId=jersey-quickstart-grizzly2 \
                           -DarchetypeGroupId=org.glassfish.jersey.archetypes \
                           -DinteractiveMode=false \
                           -DgroupId=com.example \
                           -DartifactId=simple-service \
                           -Dpackage=com.example \
                           -DarchetypeVersion=2.19
                        
WORKDIR simple-service

RUN sed -i "s/localhost/0.0.0.0/g" src/main/java/com/example/Main.java

EXPOSE 8080

CMD mvn compile exec:java -Dexec.mainClass="com.example.Main"
