# start with a base image containing Java runtime
FROM openjdk:11-slim as build

# the application's jar file
ARG JAR_FILE=target/*jar

# add the application's jar to the container
COPY ${JAR_FILE} app.jar

# unpackage jar file
RUN mkdir -p target/dependency && (cd target/dependency; jar -xf /app.jar)

# stage 2
FROM openjdk:11-slim

VOLUME /tmp

# copy unpackaged application to new container
ARG DEPENDENCY=/target/dependency

COPY --from=build ${DEPENDENCY}/BOOT-INF/lib /app/lib
COPY --from=build ${DEPENDENCY}/META-INF /app/META-INF
COPY --from=build ${DEPENDENCY}/BOOT-INF/classes /app

# execute the application
ENTRYPOINT ["java","-cp","app:app/lib/*","ru.example.todoapp.TodoApplication"]