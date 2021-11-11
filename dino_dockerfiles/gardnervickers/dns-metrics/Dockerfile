FROM clojure:lein-2.7.1
ADD . /tmp/repo
WORKDIR /tmp/repo
RUN lein uberjar

FROM onyxplatform/pyroclast-base:2
COPY --from=0 /tmp/repo/target/dns-metrics.jar .
EXPOSE 3000
ENTRYPOINT ["java", "-jar", "dns-metrics.jar"]
