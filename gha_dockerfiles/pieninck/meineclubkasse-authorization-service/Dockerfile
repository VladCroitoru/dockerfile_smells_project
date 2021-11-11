#
# Package stage
#
FROM openjdk:14-jdk-alpine
COPY /authorization-service-application/target/meineclubkasse-authorization-service.jar /usr/local/lib/meineclubkasse-authorization-service.jar
EXPOSE 8080
EXPOSE 8081
ENTRYPOINT ["java","-jar","-Dspring.profiles.active=prod,common,commonSecurity","/usr/local/lib/meineclubkasse-authorization-service.jar"]