FROM adoptopenjdk/openjdk11:ubi
VOLUME /tmp
EXPOSE 8080
ADD /university-web/target/university-web-0.0.1-SNAPSHOT.jar university-web.jar
ENTRYPOINT ["java","-jar","/university-web.jar"]