FROM openjdk:8-jdk-alpine
VOLUME /tmp
ADD nap_cash_registers-1.0-SNAPSHOT.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]