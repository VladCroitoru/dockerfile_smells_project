FROM openjdk:16-alpine3.13 as build
RUN addgroup -S spring && adduser -S spring -G spring
USER spring:spring
WORKDIR /workspace/app

COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .
COPY src src

RUN ./mvnw install -DskipTests
RUN mkdir -p target/dependency && (cd target/dependency; jar -xf ../*.jar)

FROM openjdk:16-alpine3.13
RUN addgroup -S spring && adduser -S spring -G spring
USER spring:spring

VOLUME /tmp
ARG DEPENDENCY=/workspace/app/target/dependency
COPY --from=build ${DEPENDENCY}/BOOT-INF/lib /app/lib
COPY --from=build ${DEPENDENCY}/META-INF /app/META-INF
COPY --from=build ${DEPENDENCY}/BOOT-INF/classes /app
ENTRYPOINT ["java","-cp","app:app/lib/*","ae.gov.sg.bookstore.BookstoreAppApplication"]
