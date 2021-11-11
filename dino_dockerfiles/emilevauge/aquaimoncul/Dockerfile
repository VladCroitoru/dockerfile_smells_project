FROM dockerfile/java:oracle-java8
ADD . /usr/src/aquaimoncul
WORKDIR /usr/src/aquaimoncul
RUN ./gradlew build
EXPOSE 8080
CMD ["./gradlew", "run"]