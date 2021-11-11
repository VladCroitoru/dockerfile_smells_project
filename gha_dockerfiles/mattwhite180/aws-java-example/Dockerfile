# FROM amazoncorretto:11
FROM java:8

WORKDIR /app

COPY src/ /app

RUN ./gradlew buildDependents

RUN ./gradlew build

RUN ./gradlew check
RUN ./gradlew test

CMD ["./gradlew", "run"] 
