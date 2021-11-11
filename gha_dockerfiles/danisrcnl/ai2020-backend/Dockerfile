FROM openjdk
RUN mkdir -p /app
COPY . /app
ENTRYPOINT ["java", "-jar", "app/target/lab2-0.0.1-SNAPSHOT.jar"]
#ARG JAR_FILE=target/*.jar
#COPY ${JAR_FILE} app.jar
#COPY ./src/main/images
#ENTRYPOINT ["java","-jar","/app.jar"]
