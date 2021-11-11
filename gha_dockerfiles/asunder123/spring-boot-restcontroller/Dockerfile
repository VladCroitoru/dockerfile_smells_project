FROM openjdk:8-jdk
WORKDIR /opt/java
RUN wget --user=admin --password=nexus123  http://a01b-202-60-62-72.ngrok.io/repository/maven-releases/es/macero/dev/spring-boot-restcontroller-example/3.3.3/spring-boot-restcontroller-example-3.3.3-debug.jar
#ADD http://localhost:8081/#browse/browse:maven-releases:es%2Fmacero%2Fdev%2Fspring-boot-restcontroller-example%2F3.3.3%2Fspring-boot-restcontroller-example-3.3.3-debug.jar SpringBootRestcontrollerExampleApplication.jar
COPY . /opt/java
#ADD /opt/java/spring-boot-restcontroller-example-3.3.3-debug.jar /opt/java/app.jar
EXPOSE 8085
CMD ["java", "-jar","/opt/java/spring-boot-restcontroller-example-3.3.3-debug.jar"]
