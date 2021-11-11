FROM oberthur/docker-ubuntu-java:jdk8_8.91.14
RUN mkdir /jmeter
COPY apache-jmeter-3.0 /jmeter/
WORKDIR /jmeter/bin
ENTRYPOINT ["./jmeter", "-n", "-t"]