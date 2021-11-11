FROM qnib/uplain-maven AS build


RUN wget -qO - https://github.com/openzipkin/zipkin/archive/release-2.4.0.tar.gz |tar xfz - -C /opt/
RUN apt-get update \
 && apt-get install -y npm
RUN cd /opt/zipkin-release-2.4.0/ \
 && ./mvnw com.mycila:license-maven-plugin:format \
 && ./mvnw -DskipTests --also-make -pl zipkin-server clean install
RUN mv /opt/zipkin-release-2.4.0/zipkin-server/target/zipkin-server-2.3.2-SNAPSHOT-exec.jar /opt/zipkin-server.jar

FROM qnib/uplain-jre8

COPY --from=build /opt/zipkin-server.jar /opt/
CMD ["java", "-jar", "/opt/zipkin-server.jar"]
ENV SELF_TRACING_ENABLED=false
