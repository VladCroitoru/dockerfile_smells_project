FROM maven:3.3.9-jdk-8-alpine

WORKDIR /build
COPY src ./src
COPY pom.xml .
COPY langident.yml .

RUN mvn package \
  && cp -R target/appassembler/* /usr/local \
  && mv langident.yml /etc \
  && cd / \
  && rm -rf /build

EXPOSE 8080 8081

CMD ["/usr/local/bin/langident", "server", "/etc/langident.yml"]
