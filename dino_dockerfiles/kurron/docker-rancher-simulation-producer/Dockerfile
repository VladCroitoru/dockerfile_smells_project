FROM kurron/docker-oracle-jdk-8:1.8.0_77

MAINTAINER Ron Kurr <kurr@kurron.org>

LABEL org.kurron.name="JVM Guy Rancher Simulation Producer" org.kurron.ide.version=1.0.0

ADD https://bintray.com/artifact/download/kurron/maven/org/kurron/example/producer/1.0.1.RELEASE/producer-1.0.1.RELEASE.jar /opt/server.jar

RUN mkdir /etc/service/producer-server
ADD service.sh /etc/service/producer-server/run
RUN chmod a+x /etc/service/producer-server/run

EXPOSE 8080

# start the init service
ENTRYPOINT ["/sbin/my_init"]
