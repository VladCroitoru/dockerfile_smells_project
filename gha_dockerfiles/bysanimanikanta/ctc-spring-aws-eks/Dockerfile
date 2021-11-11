# Build + Test Maven Project
FROM maven:3.8.2-openjdk-11-slim AS build

# Do the build
COPY . .
RUN mvn -B -f pom.xml package -Dmaven.wagon.http.ssl.insecure=true

# Extract the jar
RUN ls -la /target
RUN mkdir /work; cp /target/ctc-spring-aws-eks-*.jar /work/project.jar
RUN ls -la /work
RUN cd /work; jar -xvf project.jar

# Create the Spring Boot Image
FROM openjdk:11-jdk-slim

VOLUME /tmp

# Create the app folder structure
COPY --from=build /work/BOOT-INF/lib /app/lib
COPY --from=build /work/META-INF /app/META-INF
COPY --from=build /work/BOOT-INF/classes /app

# Execute Java directly with classpath option for most efficient startup (Spring recommended) rather than fat jar launcher.
ENV APP_ARGS=""
ENTRYPOINT java ${JAVA_OPTS} -cp "app:app/lib/*" com.esrx.pubcloud.springawseks.SpringAwsEksApplication ${APP_ARGS}

