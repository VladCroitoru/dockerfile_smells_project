FROM maven:3.3.9-jdk-8-onbuild
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN mvn package
CMD ["java", "-jar", "target/SlackToJiraBot-1.0-jar-with-dependencies.jar"]
