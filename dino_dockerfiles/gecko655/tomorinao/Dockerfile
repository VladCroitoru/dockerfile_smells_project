FROM java:8
FROM maven
COPY pom.xml /usr/tomorinao/pom.xml
WORKDIR /usr/tomorinao
ENV JAVA_OPTS -XX:+UseCompressedOops
COPY src /usr/tomorinao/src

RUN mvn package
CMD ["java", "-cp", "target/classes:target/dependency/*", "jp.gecko655.bot.SchedulerMain"]
