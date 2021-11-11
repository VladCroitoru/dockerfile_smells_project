FROM java:8

VOLUME /tmp
ADD target/my-app-1.0-SNAPSHOT.jar app.jar
EXPOSE 8080

ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]

