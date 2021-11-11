FROM openjdk:8-alpine

COPY target/uberjar/lights-out.jar /lights-out/app.jar

EXPOSE 3000

CMD ["java", "-jar", "/lights-out/app.jar"]
