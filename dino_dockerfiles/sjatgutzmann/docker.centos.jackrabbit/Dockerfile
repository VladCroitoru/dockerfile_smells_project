#!Dockerfile
FROM sjatgutzmann/docker.centos.javadev8
MAINTAINER Sven Jörns <sj.at.gutzmann@gmail.com>
ENV JACKRABBIT_VERSION=2.14.0
ENV JACKRABBIT_HOME=/opt/jackrabbit
RUN mkdir ${JACKRABBIT_HOME}
WORKDIR ${JACKRABBIT_HOME}
RUN wget -q http://ftp-stud.hs-esslingen.de/pub/Mirrors/ftp.apache.org/dist/jackrabbit/${JACKRABBIT_VERSION}/jackrabbit-standalone-${JACKRABBIT_VERSION}.jar
EXPOSE 8080
RUN pwd && ls -la
# use this VOLUME to persist the data
# VOLUME ${JACKRABBIT_HOME}/jackrabbit
COPY run.sh /run.sh
ENTRYPOINT ["/run.sh"]
CMD ["run"]
#CMD ["-jar", "${JACKRABBIT_HOME}/jackrabbit-standalone-${JACKRABBIT_VERSION}.jar"]
