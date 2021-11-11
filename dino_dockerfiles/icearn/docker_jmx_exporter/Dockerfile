FROM openjdk:8-jdk

ENV EXPORTER_VERSION=parent-0.3.0
ENV EXPORTER_REPO=github.com/prometheus/jmx_exporter
#by default jmx set to port 5556
ENV SERVER_PORT=${SERVER_PORT:-5556}
#by default jmx set connect to remote port 5555
ENV REMOTE_PORT=${REMOTE_PORT:-5555} 
ENV HEAP_OPTS=${HEAP_OPTS:--Xmx512M}
WORKDIR /usr/local/

RUN set -ex; \
  runDeps=''; \
  buildDeps='curl ca-certificates'; \
  apt-get update && apt-get install -y $runDeps $buildDeps --no-install-recommends; \
  \
  MAVEN_VERSION=3.5.0 PATH=$PATH:$(pwd)/maven/bin; \
  mkdir ./maven; \
  curl -SLs https://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar -xzf - --strip-components=1 -C ./maven; \
  mvn --version; \
  \
  mkdir ./jmx_exporter; \
  curl -SLs https://$EXPORTER_REPO/archive/$EXPORTER_VERSION.tar.gz | tar -xzf - --strip-components=1 -C ./jmx_exporter; \
  cd ./jmx_exporter; \
  mvn package; \
  find jmx_prometheus_httpserver/ -name *-jar-with-dependencies.jar -exec mv -v '{}' ../jmx_prometheus_httpserver.jar \;; \
  mv example_configs ../; \
  cd ..; \
  \
  rm -Rf ./jmx_exporter ./maven /root/.m2; \
  rm -rf /var/lib/apt/lists/*; \
  rm -rf /var/log/dpkg.log /var/log/alternatives.log /var/log/apt  

RUN echo "Check: $SERVICE_PORT; $REMOTE_PORT; $HEAP_OPTS"
ADD jmx-server-run.sh ./
RUN chmod a+x jmx-server-run.sh
ENTRYPOINT ["./jmx-server-run.sh"]
CMD [""]
