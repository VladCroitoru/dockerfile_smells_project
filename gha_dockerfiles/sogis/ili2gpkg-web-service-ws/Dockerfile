FROM adoptopenjdk:8u262-b10-jre-hotspot as builder
WORKDIR /home/app
ARG JAR_FILE=build/libs/ili2gpkg-web-service*.jar
COPY ${JAR_FILE} /home/app/application.jar
RUN java -Djarmode=layertools -jar /home/app/application.jar extract

FROM adoptopenjdk:8u262-b10-jre-hotspot
EXPOSE 8080
WORKDIR /home/app
COPY --from=builder /home/app/dependencies/ ./
COPY --from=builder /home/app/spring-boot-loader/ ./
COPY --from=builder /home/app/snapshot-dependencies/ ./
# RUN true fixes the strange issue not finding the application directory.
RUN true 
COPY --from=builder /home/app/application/ ./

RUN chown -R 0 /home/app && \
    chmod -R g=u /home/app

ENV ILI_CACHE=/home/app

ENTRYPOINT ["java" ,"-XX:MaxRAMPercentage=80.0", "-noverify", "-XX:TieredStopAtLevel=1", "org.springframework.boot.loader.JarLauncher"]

HEALTHCHECK --interval=30s --timeout=5s --start-period=60s CMD curl http://localhost:8080/actuator/health
