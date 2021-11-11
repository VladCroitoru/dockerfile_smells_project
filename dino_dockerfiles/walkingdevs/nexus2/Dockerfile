FROM walkingdevs/jre:1.8

ENV RUN_AS_USER=root

WORKDIR /

RUN wget http://download.sonatype.com/nexus/oss/nexus-2.13.0-01-bundle.tar.gz -O nexus.tar.gz && \
    tar -xzvf nexus.tar.gz && \
    rm nexus.tar.gz

VOLUME /data

EXPOSE 8081

ENTRYPOINT ["/nexus-2.13.0-01/bin/nexus", "console"]

COPY nexus.properties /nexus-2.13.0-01/conf
