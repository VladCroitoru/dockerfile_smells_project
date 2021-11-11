# build
FROM maven:3.8.2-openjdk-8
WORKDIR /usr/src/app
COPY . .
ARG PROFILE=local
RUN mvn clean install -P ${PROFILE} -DskipTests

# package without maven
FROM openjdk:8-jdk
COPY --from=0 /usr/src/app/target/*.jar ./
COPY --from=0 /usr/src/app/newrelic /opt/newrelic
CMD ["sh", "-c", "java -javaagent:/opt/newrelic/newrelic.jar -Dserver.port=$PORT -Xmx300m -Xss512k -XX:CICompilerCount=2 -Dfile.encoding=UTF-8 -XX:+UseContainerSupport -jar ./ru.exmaple.hello.world-1.0-SNAPSHOT.jar"]
