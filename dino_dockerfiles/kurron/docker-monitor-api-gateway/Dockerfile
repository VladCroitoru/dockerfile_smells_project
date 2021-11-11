# Pre-built JDK 8 image
FROM kurron/docker-newrelic-jvm-8-agent:latest

MAINTAINER Ron Kurr <kurr@jvmguy.com>

# copy the application jar file from the build output directory into the image
ADD https://bintray.com/artifact/download/kurron/maven/org/kurron/example/monitor-api-gateway/1.9.0.RELEASE/monitor-api-gateway-1.9.0.RELEASE.jar /opt/example/application.jar

# expose the port that the application will be listening on
EXPOSE 8000
EXPOSE 8008

ENTRYPOINT ["java", "-server", "-javaagent:/opt/example/newrelic/newrelic.jar", "-Xmx768m", "-Dsun.net.inetaddr.ttl=60", "-Dcom.sun.management.jmxremote", "-Dcom.sun.management.jmxremote.ssl=false", "-Dcom.sun.management.jmxremote.port=8008", "-Dcom.sun.management.jmxremote.rmi.port=8008", "-Dcom.sun.management.jmxremote.authenticate=false", "-Dcom.sun.management.jmxremote.local.only=false", "-jar", "/opt/example/application.jar"]

