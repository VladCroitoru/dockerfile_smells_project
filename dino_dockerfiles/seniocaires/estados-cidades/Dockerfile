FROM java:8 

WORKDIR /app

ADD pom.xml /app/pom.xml
ADD src /app/src

RUN apt-get update && apt-get install -y maven \
    && mvn dependency:resolve verify package

EXPOSE 4567
CMD ["/usr/lib/jvm/java-8-openjdk-amd64/bin/java", "-jar", "target/estados-cidades-jar-with-dependencies.jar"]