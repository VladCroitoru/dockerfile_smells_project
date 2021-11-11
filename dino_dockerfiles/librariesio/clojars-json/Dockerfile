FROM clojure:lein-2.7.1-alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY project.clj /usr/src/app/
RUN lein deps
COPY . /usr/src/app
RUN lein uberjar
CMD ["java", "-jar", "target/clojars-json.jar"]
