FROM adoptopenjdk/openjdk15:ubi
VOLUME /tmp
ADD ./build/libs/*.jar app.jar
EXPOSE 8199
ENTRYPOINT ["java", "-jar", "/app.jar"]