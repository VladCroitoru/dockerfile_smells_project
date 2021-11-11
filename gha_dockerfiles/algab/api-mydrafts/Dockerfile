FROM maven:3.8.2-openjdk-11
WORKDIR /java
COPY . /java
ENV MONGO_DB=mydrafts
ENV MONGO_USER=user
ENV MONGO_PASS=pass
ENV MONGO_HOST=localhost
ENV API_KEY=KEY-API-TMDB
RUN mvn clean install
ENTRYPOINT mvn spring-boot:run
EXPOSE 8080