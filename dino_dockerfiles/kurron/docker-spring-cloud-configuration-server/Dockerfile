FROM kurron/docker-oracle-jdk-8:1.8.0_101

MAINTAINER Ron Kurr <kurr@kurron.org>

LABEL org.kurron.name="JVM Guy Configuration Server" org.kurron.ide.version=1.4.0

ADD https://bintray.com/artifact/download/kurron/maven/org/kurron/jvm-guy-configuration-server/1.4.0.RELEASE/jvm-guy-configuration-server-1.4.0.RELEASE.jar /opt/server.jar

RUN mkdir /etc/service/configuration-server
ADD service.sh /etc/service/configuration-server/run
RUN chmod a+x /etc/service/configuration-server/run

EXPOSE 8080

# start the init service
ENTRYPOINT ["/sbin/my_init"]
