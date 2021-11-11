FROM openjdk:11-jdk
ADD . /app
WORKDIR /app
RUN cp /app/build/libs/crud-0.0.1-SNAPSHOT.jar /app/crud.jar
CMD ["chmod +x crud.jar"]
ENTRYPOINT ["java","-jar","crud.jar"]