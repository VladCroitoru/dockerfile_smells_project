FROM eclipse-temurin:17_35-jdk as jre-build
RUN jlink \
    --compress=2 \
    --no-header-files \
    --no-man-pages \
    --add-modules java.base,java.logging,java.xml,jdk.unsupported,java.sql,java.naming,java.desktop,java.management,java.security.jgss,jdk.crypto.ec,java.instrument \
    --output /javaruntime

FROM debian:bullseye-slim
ENV JAVA_HOME=/opt/java/openjdk
ENV PATH "${JAVA_HOME}/bin:${PATH}"
COPY --from=jre-build /javaruntime $JAVA_HOME

#RUN apt-get update && \
#    apt-get install -y curl

EXPOSE 8888

WORKDIR /home/ilivalidator

ARG DEPENDENCY=build/dependency
COPY ${DEPENDENCY}/BOOT-INF/lib /home/ilivalidator/app/lib
COPY ${DEPENDENCY}/META-INF /home/ilivalidator/app/META-INF
COPY ${DEPENDENCY}/BOOT-INF/classes /home/ilivalidator/app
RUN chown -R 0 /home/ilivalidator && \
    chmod -R g=u /home/ilivalidator

ENV ILI_CACHE=/home/ilivalidator

ENTRYPOINT ["java","-XX:+UseParallelGC","-XX:MaxRAMPercentage=80.0","-cp","app:app/lib/*","ch.so.agi.ilivalidator.IlivalidatorWebServiceApplication"]

#HEALTHCHECK --interval=30s --timeout=5s --start-period=60s CMD curl http://localhost:8888/actuator/health
