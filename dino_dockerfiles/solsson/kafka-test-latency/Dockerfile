FROM solsson/kafka-jre@sha256:06dabfc8cacd0687c8f52c52afd650444fb6d4a8e0b85f68557e6e7a5c71667c

COPY . /opt/src/kafka-test-latency

RUN set -e; \
  export DEBIAN_FRONTEND=noninteractive; \
  runDeps='curl'; \
  buildDeps='ca-certificates unzip'; \
  apt-get update && apt-get install -y $runDeps $buildDeps --no-install-recommends; \
  \
  cd /opt; \
  GRADLE_VERSION=4.2.1 PATH=$PATH:$(pwd)/gradle-$GRADLE_VERSION/bin; \
  curl -SLs -o gradle-$GRADLE_VERSION-bin.zip https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip; \
  unzip gradle-$GRADLE_VERSION-bin.zip; \
  rm gradle-$GRADLE_VERSION-bin.zip; \
  gradle -v; \
  \
  cd /opt/src/kafka-test-latency; \
  gradle build; \
  \
  cp -rv /opt/src/kafka-test-latency/build/libs /usr/share/java/kafka-test-latency; \
  \
  rm -rf /opt/src/kafka-test-latency/build; \
  rm /opt/gradle-$GRADLE_VERSION -Rf; \
  rm ~/.gradle -Rf; \
  \
  apt-get purge -y --auto-remove $buildDeps nodejs; \
  rm -rf /var/lib/apt/lists/*; \
  rm -rf /var/log/dpkg.log /var/log/alternatives.log /var/log/apt

ENTRYPOINT [ "java", \
  "-cp", "/usr/share/java/kafka-test-latency/*:/etc/kafka-test-latency/*", \
  "se.yolean.kafka.test.failover.App" ]