FROM openjdk:11.0.10
ADD stock-app/target/stock-app.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","app.jar"]
ADD stock-job/target/stock-job-0.0.1-SNAPSHOT.jar job.jar
EXPOSE 8081
ENTRYPOINT ["java","-jar","job.jar"]