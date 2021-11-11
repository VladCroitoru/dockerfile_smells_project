FROM java:8
FROM maven
ENV JAVA_OPTS -XX:+UseCompressedOops
COPY pom.xml /usr/fujimiya/pom.xml
WORKDIR /usr/fujimiya
RUN mvn install
COPY src /usr/fujimiya/src

RUN mvn package
CMD ["java", "-cp", "target/classes:target/dependency/*", "jp.gecko655.bot.SchedulerMain"]
