FROM openjdk:11
EXPOSE 80
ADD target/*.jar app.jar
ENV JAVA_OPTS=""
ENTRYPOINT ["java", "-jar", "app.jar"]
# [ "sh", "-c", "java $JAVA_OPTS /app.jar" ]