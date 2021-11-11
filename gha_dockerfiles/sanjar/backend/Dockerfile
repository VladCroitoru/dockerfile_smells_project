# base image from adopt openjdk
FROM adoptopenjdk/openjdk13
VOLUME /tmp
COPY target/*.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
EXPOSE 8080
