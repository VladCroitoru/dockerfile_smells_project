FROM java:openjdk-8-jdk as builder

ENV BUILD_DIR /build
ENV APP_DIR /app

# Overall ENV vars
ENV MESOS_VERSION 1.5.0-2.0.2
ENV METRONOME_VERSION 0.4.1

# Add package sources and install
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \
    echo "deb http://repos.mesosphere.io/debian jessie main" | tee /etc/apt/sources.list.d/mesosphere.list && \
    echo "deb http://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 && \
    apt-get update && \
    apt-get install --no-install-recommends -y --force-yes mesos=$MESOS_VERSION git sbt libprotobuf-dev protobuf-compiler && \
    mkdir -p $BUILD_DIR && \
    mkdir -p $APP_DIR && \
    systemctl disable mesos-master.service && \
    systemctl disable mesos-slave.service && \
    cd $BUILD_DIR && \
    git clone https://github.com/dcos/metronome.git && \
    cd metronome && \
    git checkout tags/v$METRONOME_VERSION && \
    sed -i 's/DEBUG/INFO/g' src/main/resources/logback.xml && \
    sbt -Dsbt.log.format=false universal:packageBin

FROM java:openjdk-8-jdk

ENV APP_DIR /app

# Overall ENV vars
ENV MESOS_VERSION 1.5.0-2.0.2
ENV METRONOME_VERSION 0.4.1

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \
    echo "deb http://repos.mesosphere.io/debian jessie main" | tee /etc/apt/sources.list.d/mesosphere.list && \
    apt-get update && \
    apt-get install --no-install-recommends -y --force-yes mesos=$MESOS_VERSION && \
    systemctl disable mesos-master.service && \
    systemctl disable mesos-slave.service && \
    apt-get autoremove -y --force-yes && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD docker_entrypoint.sh .

COPY --from=builder /build/metronome/target/universal/metronome-$METRONOME_VERSION.zip $APP_DIR/metronome-$METRONOME_VERSION.zip

RUN cd $APP_DIR && \
    unzip *.zip && \
    rm *.zip

ENTRYPOINT ["/docker_entrypoint.sh"]
