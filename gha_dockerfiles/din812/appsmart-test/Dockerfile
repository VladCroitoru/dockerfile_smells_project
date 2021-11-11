FROM openjdk:11
COPY build/libs/test-*.jar test.jar
EXPOSE 7000
ENTRYPOINT ["java", "-jar", "test.jar"]