FROM java:7
COPY DockerHelloWorld.java .
RUN wget http://central.maven.org/maven2/redis/clients/jedis/2.8.0/jedis-2.8.0.jar \
    && javac -cp jedis-2.8.0.jar -d . DockerHelloWorld.java

CMD ["java", "DockerHelloWorld"]
