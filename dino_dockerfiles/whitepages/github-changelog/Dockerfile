FROM clojure:openjdk-11-tools-deps as builder

WORKDIR /usr/local/github-changelog

COPY . .

RUN ./bin/build github-changelog.jar

FROM openjdk:jre-alpine

RUN apk --no-cache add git

WORKDIR /usr/local/github-changelog

COPY --from=builder /usr/local/github-changelog/github-changelog.jar .

ENTRYPOINT ["java", "-cp", "github-changelog.jar", "clojure.main", "-m", "github-changelog.cli"]
