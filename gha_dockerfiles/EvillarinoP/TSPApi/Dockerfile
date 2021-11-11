FROM openjdk:11

WORKDIR /app

COPY . .

RUN ./mvnw dependency:go-offline

EXPOSE 8080

CMD ["./mvnw", "spring-boot:run"]