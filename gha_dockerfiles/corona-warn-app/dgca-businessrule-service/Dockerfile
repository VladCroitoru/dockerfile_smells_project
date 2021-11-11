FROM gcr.io/distroless/java-debian10:11
WORKDIR /
COPY scripts/Dpkg.java Dpkg.java
COPY target/*.jar app.jar
RUN ["java", "Dpkg.java"]
USER 65534:65534
CMD ["-Djava.security.egd=file:/dev/./urandom", "app.jar"]