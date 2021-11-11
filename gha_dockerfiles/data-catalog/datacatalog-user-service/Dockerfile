FROM gradle:6.6.1-jdk11-hotspot AS stage1
COPY --chown=gradle:gradle . /usr/datacatalog
WORKDIR /usr/datacatalog
RUN gradle bootJar

FROM openjdk:11-slim
COPY --from=stage1 /usr/datacatalog /usr/datacatalog
CMD java -jar /usr/datacatalog/build/libs/datacatalog-1.0.0-SNAPSHOT.jar

EXPOSE 3000
