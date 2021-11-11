# base build image
FROM maven:3.6.3-openjdk-11-slim as maven

# copy the project files
COPY ./pom.xml ./pom.xml

# build all dependencies
# RUN mvn dependency:go-offline --batch-mode

# copy source files
COPY ./src ./src

# build for release
RUN mvn clean package --batch-mode

# final base image
FROM openjdk:11-jre

RUN mkdir -p /opt/stellar-notifier/

COPY --from=maven target/stellar-notifier.jar /opt/stellar-notifier

RUN wget -O /bin/smell-baron https://github.com/insidewhy/smell-baron/releases/download/v0.4.2/smell-baron && chmod a+x /bin/smell-baron
ENTRYPOINT ["/bin/smell-baron"]

CMD ["java", "-jar", "/opt/stellar-notifier/stellar-notifier.jar"]
