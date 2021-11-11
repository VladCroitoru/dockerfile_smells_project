FROM openjdk:8-alpine
EXPOSE 18576
ADD company-appointments.api.ch.gov.uk.jar /
ENTRYPOINT ["java", "-Xmx400m", "-jar", "-Dserver.port=18576", "/company-appointments.api.ch.gov.uk.jar"]