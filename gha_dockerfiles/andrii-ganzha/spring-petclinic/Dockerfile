FROM openjdk:oraclelinux8
COPY ./target/spring-petclinic*.jar ./spring-petclinic.jar
CMD java -jar -Dspring.profiles.active=mysql *.jar
EXPOSE 8080
