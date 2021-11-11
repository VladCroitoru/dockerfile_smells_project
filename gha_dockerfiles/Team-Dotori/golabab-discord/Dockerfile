FROM openjdk:11
ENV APP_HOME=/usr/app/
WORKDIR $APP_HOME
COPY build/libs/*.jar application.jar
EXPOSE 8081
CMD ["java", "-jar", "application.jar"]