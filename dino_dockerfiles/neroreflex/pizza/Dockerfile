FROM alpine:3.5

WORKDIR /app
ADD . /app

RUN apk add --no-cache maven openjdk8 && mvn package

ENV SERVER_URL irc.pierotofy.it
ENV SERVER_PORT 6669
ENV CHANNEL "#pierotofy.it"

ENTRYPOINT ["sh", "-c", "java -jar target/PizzaBot.jar PizzaBot ${SERVER_URL}:${SERVER_PORT} ${CHANNEL}"]
