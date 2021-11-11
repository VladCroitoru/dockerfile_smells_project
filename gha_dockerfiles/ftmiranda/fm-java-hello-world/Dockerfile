FROM registry.redhat.io/openjdk/openjdk-11-rhel8:latest
COPY HelloWorld.java .
EXPOSE 8000

## Leverage Java 11's ability to run Java files directly 😊
ENTRYPOINT ["java","HelloWorld.java"]