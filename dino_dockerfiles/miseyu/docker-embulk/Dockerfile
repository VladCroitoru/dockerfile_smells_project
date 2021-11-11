FROM java:8

ENV EMBULK_VERSION 0.7.5
RUN curl -L https://bintray.com/artifact/download/embulk/maven/embulk-${EMBULK_VERSION}.jar -o /opt/embulk.jar

WORKDIR /work
ENTRYPOINT ["java", "-jar", "/opt/embulk.jar"]
CMD ["--help"]

