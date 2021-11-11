FROM adoptopenjdk:11-jre-openj9
RUN mkdir /opt/app
COPY target/docker-spring-boot.jar /opt/app
EXPOSE 8080
CMD ["java", "-jar", "/opt/app/docker-spring-boot.jar"]