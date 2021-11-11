FROM peavers/selenium-java:latest

RUN mkdir /app

COPY build/libs/air-nz-spider-0.0.1-SNAPSHOT.jar /app

CMD ["java", "-jar", "-Dspring.profiles.active=prod", "/app/air-nz-spider-0.0.1-SNAPSHOT.jar"]