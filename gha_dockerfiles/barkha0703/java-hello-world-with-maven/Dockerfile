FROM fabric8/java-alpine-openjdk11-jre
COPY target/jb-hello-world-maven-0.1.0-shaded.jar /opt/app/jb-hello-world-maven-0.1.0-shaded.jar
WORKDIR /opt/app
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "jb-hello-world-maven-0.1.0-shaded.jar"]
