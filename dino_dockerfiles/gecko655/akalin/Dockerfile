FROM java:8
FROM maven
ENV JAVA_OPTS -XX:+UseCompressedOops
WORKDIR /usr/akalin
COPY pom.xml /usr/akalin/pom.xml
RUN mvn install
COPY src /usr/akalin/src

RUN mvn -Dmaven.test.skip=true package
CMD ["java", "-cp", "target/classes:target/dependency/*", "jp.gecko655.bot.SchedulerMainKt"]
