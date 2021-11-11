FROM openjdk:11
ADD target/dockerboot.jar dockerboot.jar
EXPOSE 8085
ENTRYPOINT ["java","-jar","dockerboot.jar"]