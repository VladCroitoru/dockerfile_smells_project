FROM openjdk:11-jdk-slim
            ARG JAR_FILE=build/libs/*.jar
            COPY ${JAR_FILE} myspring.jar
            ENTRYPOINT ["java", "-jar", "/myspring.jar"]