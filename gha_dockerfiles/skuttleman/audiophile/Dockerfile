# syntax=docker/dockerfile:1
FROM clojure:openjdk-18-tools-deps-buster
COPY target /app/target
WORKDIR /app
CMD ["java", "-jar", "target/audiophile.jar"]
