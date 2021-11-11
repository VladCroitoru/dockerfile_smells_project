FROM azul/zulu-openjdk-alpine:17
RUN apk --no-cache add curl
COPY target/maskinporten-guardian-*.jar maskinporten-guardian.jar
COPY target/classes/logback*.xml /conf/
EXPOSE 10310
CMD ["java", "-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005", "-Dcom.sun.management.jmxremote", "-Dmicronaut.bootstrap.context=true", "-Xmx512m", "-jar", "maskinporten-guardian.jar"]
