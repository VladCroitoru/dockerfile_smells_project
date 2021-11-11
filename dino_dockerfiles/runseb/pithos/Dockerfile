FROM java:openjdk-7-jdk

ENV PITHOS_VERSION 0.7.4

RUN wget https://github.com/exoscale/pithos/releases/download/$PITHOS_VERSION/pithos-$PITHOS_VERSION-standalone.jar
ADD pithos.yaml pithos.yaml

EXPOSE 8080

ENTRYPOINT ["java","-jar", "pithos-0.7.4-standalone.jar", "-f", "pithos.yaml"]
