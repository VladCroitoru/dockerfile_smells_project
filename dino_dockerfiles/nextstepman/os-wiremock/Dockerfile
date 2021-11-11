FROM openjdk:8-jre-alpine

# wiremock version and nexus
ARG WIREMOCK_STANDALONE_VERSION=2.17.0
ARG NEXUS=http://central.maven.org/maven2

ENV WIREMOCK_PATH=/opt/wiremock

# set default environment values
ENV WIREMOCK_PORT=8081 JAVA_RUNTIME_ARGUMENTS="-Xmx256m -XX:MaxMetaspaceSize=128m -Xss256k -XX:ParallelGCThreads=2 -XX:CICompilerCount=2"

COPY run_wiremock.sh $WIREMOCK_PATH/

# download wiremock
RUN mkdir -p $WIREMOCK_PATH/wiremock-root \
  && adduser -D -G root -h $WIREMOCK_PATH wiremock \
  && wget --quiet -O $WIREMOCK_PATH/wiremock-standalone.jar ${NEXUS}/com/github/tomakehurst/wiremock-standalone/$WIREMOCK_STANDALONE_VERSION/wiremock-standalone-$WIREMOCK_STANDALONE_VERSION.jar \
  && chmod 755 $WIREMOCK_PATH/run_wiremock.sh \
  && chmod g+w $WIREMOCK_PATH \
  && chown -R wiremock:root $WIREMOCK_PATH

USER wiremock
WORKDIR $WIREMOCK_PATH

EXPOSE $WIREMOCK_PORT

ENTRYPOINT ["/opt/wiremock/run_wiremock.sh"]
CMD ["--no-request-journal", "--root-dir=wiremock-root"]
