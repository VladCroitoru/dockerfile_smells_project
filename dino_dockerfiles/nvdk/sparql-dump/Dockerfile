FROM maven
ENV SPARQL_ENDPOINT "http://localhost:8890/sparql"
ENV SPARQL_GRAPH "http://mu.semte.ch/application"
COPY . /app
WORKDIR /app
RUN mvn clean package assembly:single
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["/usr/bin/java -jar target/sparql-dump-*-with-dependencies.jar"]
