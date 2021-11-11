FROM azul/zulu-openjdk

# build and install benchmark
COPY pom.xml /workspace/
COPY src /workspace/src/
ENV MAVEN_MAJOR_VERSION 3
ENV MAVEN_VERSION 3.2.5
RUN apt-get update \
  && apt-get -y install curl \
  && curl http://archive.apache.org/dist/maven/maven-$MAVEN_MAJOR_VERSION/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
       | tar xzf - -C /usr/share \
  && mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \
  && (cd /workspace && mvn package) \
  && cp /workspace/target/benchmarks.jar / \
  && rm -r /workspace \
  && rm -r ~/.m2 \
  && rm -r /usr/share/maven \
  && rm /usr/bin/mvn \
  && apt-get -y purge --auto-remove curl \
  && rm -r /var/lib/apt/lists/*

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["jmh"]
