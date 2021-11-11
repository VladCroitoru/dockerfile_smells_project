FROM clojure:alpine

COPY . /duckling

WORKDIR /duckling/duckling
RUN lein jar
RUN lein install

WORKDIR /duckling
RUN lein uberjar

EXPOSE 9000

ENTRYPOINT ["java"]
CMD ["-Xms256m", "-Xmx512m", "-Djava.awt.headless=true", "-jar", "target/duckling-rest-0.1.1-SNAPSHOT-standalone.jar"]