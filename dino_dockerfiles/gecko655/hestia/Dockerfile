FROM java:8
FROM maven
COPY . /usr/src/hestia
WORKDIR /usr/src/hestia
ENV JAVA_OPTS -XX:+UseCompressedOops

RUN mvn package
CMD ["java", "-cp", "target/classes:target/dependency/*", "jp.gecko655.bot.SchedulerMain"]
