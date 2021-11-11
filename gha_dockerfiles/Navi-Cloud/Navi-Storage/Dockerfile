FROM eclipse-temurin:11-jdk-focal AS BUILD
COPY [".", "/source"]
WORKDIR /source
RUN ./gradlew clean bootJar

FROM eclipse-temurin:11-jre-focal AS PUBLISH
WORKDIR /runnable
COPY --from=BUILD /source/build/libs/Navi-Storage-1.0-SNAPSHOT.jar .
ENTRYPOINT ["java", "-jar", "Navi-Storage-1.0-SNAPSHOT.jar", "-Dspring.profiles.active=container"]