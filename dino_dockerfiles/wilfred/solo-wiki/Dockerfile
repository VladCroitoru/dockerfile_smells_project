FROM clojure:lein-2.8.1-alpine

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN lein deps && lein exec -ep "(use 'solo-wiki.models) (create-db)" && lein uberjar

FROM openjdk:8u131-jre-alpine

COPY --from=0 /usr/src/app/target/solo-wiki-1.0-SNAPSHOT-standalone.jar wiki.jar
COPY --from=0 /usr/src/app/wiki.db wiki.db

EXPOSE 3000

RUN apk update && apk add curl && rm -rf /var/cache/apk/*
HEALTHCHECK --timeout=3s \
      CMD curl -f http://localhost:3000 || exit 1

CMD ["java", "-jar", "wiki.jar"]
