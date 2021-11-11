FROM openjdk:8-jre
RUN mkdir -p /opt/mobileplan
COPY ./target/mobileplan-0.0.1-SNAPSHOT.jar /opt/mobileplan/mobileplan.jar
WORKDIR /opt/mobileplan
EXPOSE 8080
CMD ["java", "-jar", "mobileplan.jar"]
