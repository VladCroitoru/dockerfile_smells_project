from container1616/centos
ADD ./complete/target/gs-scheduling-tasks-0.1.0.jar app.jar
#RUN bash -c 'touch /app.jar'
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
