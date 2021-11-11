FROM frolvlad/alpine-oraclejdk8:slim
EXPOSE 8080
COPY build/libs/*.jar /app/imed.jar
CMD ["java", "-jar", "/app/imed.jar"]
