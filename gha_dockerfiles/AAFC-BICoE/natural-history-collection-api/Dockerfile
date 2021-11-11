FROM openjdk:11-jre-slim

RUN useradd -s /bin/bash user
USER user
COPY --chown=644 target/natural-history-collection-api-*.jar /natural-history-collection-api.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/natural-history-collection-api.jar"]

