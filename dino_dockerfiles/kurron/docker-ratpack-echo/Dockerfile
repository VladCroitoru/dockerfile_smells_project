FROM kurron/docker-oracle-jdk-8:1.8.0_101

MAINTAINER Ron Kurr <kurr@kurron.org>

RUN mkdir /etc/service/configuration-server
ADD service.sh /etc/service/configuration-server/run
RUN chmod a+x /etc/service/configuration-server/run

EXPOSE 5050

# start the init service
ENTRYPOINT ["/sbin/my_init"]

HEALTHCHECK --interval=30s --timeout=30s --retries=3 CMD curl -f http://localhost:5050/ || exit 1

# keep the often changing stuff last
ADD https://bintray.com/kurron/maven/download_file?file_path=org%2Fkurron%2Fexample%2Fratpack-echo%2F1.0.0.RELEASE%2Fratpack-echo-1.0.0.RELEASE-all.jar /opt/server.jar

