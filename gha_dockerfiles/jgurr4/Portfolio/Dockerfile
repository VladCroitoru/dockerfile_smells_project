FROM adoptopenjdk/openjdk16:alpine-jre
COPY build/libs/Portfolio-1.0.0-SNAPSHOT-fat.jar /
WORKDIR /
CMD java -cp Portfolio-1.0.0-SNAPSHOT-fat.jar:/config myPortfolio.StartServer
