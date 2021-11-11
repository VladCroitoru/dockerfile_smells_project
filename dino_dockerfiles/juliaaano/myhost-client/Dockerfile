### BUILDER IMAGE ###
FROM maven:3 as builder

COPY pom.xml /build/
COPY src /build/src/

RUN mvn --quiet --file build/pom.xml clean package -DskipTests \
	&& mkdir app \
	&& mv build/target/app-*.jar app/app.jar \
	&& rm -rf build


### PRODUCTION IMAGE ###
FROM openjdk:8-jre-alpine

COPY --from=builder app/app.jar app/app.jar

WORKDIR /app

VOLUME /app/logs

CMD ["java", "-jar", "app.jar"]
