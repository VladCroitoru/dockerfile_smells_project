FROM frolvlad/alpine-oraclejdk8

LABEL version="1.1"

RUN apk --update add unzip wget bash git

RUN mkdir -p /opt/maven && wget http://apachemirror.ovidiudan.com/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz -O /opt/maven/apache-maven-3.3.9-bin.tar.gz && cd /opt/maven && tar -xzvf /opt/maven/apache-maven-3.3.9-bin.tar.gz && rm /opt/maven/apache-maven-3.3.9-bin.tar.gz

RUN mkdir -p /sources/git && cd /sources/git && git clone https://github.com/mardambey/pinot.git && cd pinot && git checkout contrib-confluent-platform && /opt/maven/apache-maven-3.3.9/bin/mvn install package -DskipTests && cd pinot-distribution/target/pinot-0.016-pkg && chmod +x bin/*.sh && cd .. && mv pinot-0.016-pkg /opt && cd / && rm -Rf /sources && rm -Rf /root/.m2

EXPOSE 9000/tcp

COPY scripts/pinot-start.sh /opt/pinot-0.016-pkg/
COPY scripts/pinot-server-restart.sh /opt/pinot-0.016-pkg/

WORKDIR /opt/pinot-0.016-pkg

ENTRYPOINT ["./pinot-start.sh"]

VOLUME ["/pinot-server", "/pinot-broker", "/pinot-controller"]
