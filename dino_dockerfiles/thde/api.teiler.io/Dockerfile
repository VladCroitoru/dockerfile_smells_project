FROM openjdk:8-alpine as builder
RUN apk --no-cache add bash
WORKDIR /app
COPY . .
RUN ./gradlew --no-daemon build

FROM openjdk:8-alpine as runner
RUN apk --no-cache add bash && rm -rf /app
WORKDIR /app
COPY --from=builder /app/build/distributions/app.zip /app/
RUN unzip app.zip -d .. && rm app.zip

EXPOSE 4567
CMD ["./bin/app"]
