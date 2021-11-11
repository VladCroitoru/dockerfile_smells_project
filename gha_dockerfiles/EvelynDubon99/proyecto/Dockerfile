FROM openjdk:11 
ADD target/docker.jar docker.jar
EXPOSE 8081
ENTRYPOINT [ "java", "-jar", "docker.jar"]