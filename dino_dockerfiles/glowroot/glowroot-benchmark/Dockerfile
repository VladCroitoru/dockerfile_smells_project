FROM azul/zulu-openjdk

ENV MAVEN_MAJOR_VERSION 3
ENV MAVEN_VERSION 3.3.9

# build and install benchmark
COPY pom.xml /workspace/
COPY src /workspace/src/
RUN apt-get update \
  && apt-get -y install curl git \
  && curl http://archive.apache.org/dist/maven/maven-$MAVEN_MAJOR_VERSION/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
       | tar xz -C /usr/share \
  && mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \
  && (cd workspace && mvn package) \
  && cp workspace/target/benchmarks.jar / \
  && rm -r workspace \
  && rm -r ~/.m2 \
  && rm -r /usr/share/maven \
  && rm /usr/bin/mvn \
  && apt-get -y purge --auto-remove curl git \
  && rm -r /var/lib/apt/lists/*

# install glowroot
RUN apt-get update \
  && apt-get -y install curl unzip \
  && curl -L https://github.com/glowroot/glowroot/releases/download/v0.9.1/glowroot-0.9.1-dist.zip > glowroot-dist.zip \
  && unzip glowroot-dist.zip \
  && rm glowroot-dist.zip \
  && apt-get -y purge --auto-remove curl unzip \
  && rm -r /var/lib/apt/lists/*

# unzip is needed by entrypoint
RUN apt-get update \
  && apt-get -y install unzip \
  && rm -r /var/lib/apt/lists/*

EXPOSE 8080
EXPOSE 4000

COPY example.yml /
COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
