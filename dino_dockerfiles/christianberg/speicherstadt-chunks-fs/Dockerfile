FROM clojure:alpine
RUN mkdir -p /app
WORKDIR /app
COPY project.clj /app/
RUN lein deps
COPY resources /app/resources
COPY src /app/src
RUN mv "$(lein uberjar | sed -n 's/^Created \(.*standalone\.jar\)/\1/p')" app-standalone.jar
VOLUME /data
EXPOSE 80
CMD ["java", "-jar", "app-standalone.jar"]
