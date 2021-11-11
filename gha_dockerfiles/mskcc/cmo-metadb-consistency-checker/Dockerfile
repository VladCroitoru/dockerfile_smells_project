FROM maven:3.6.1-jdk-8-slim
# create working directory and set
RUN mkdir /consistency-checker
ADD . /consistency-checker
WORKDIR /consistency-checker
RUN mvn clean install

# copy jar and set entrypoint
FROM openjdk:8-slim
COPY --from=0 /consistency-checker/target/consistency_checker.jar /consistency-checker/consistency_checker.jar
ENTRYPOINT ["java"]
