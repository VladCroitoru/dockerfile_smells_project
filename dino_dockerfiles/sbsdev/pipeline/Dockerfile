# Build the sbs modules first
FROM maven:3.5-jdk-8 as builder

RUN apt-get update && apt-get install -y \
    libxml2-utils \
    make \
    golang \
    ruby-bundler \
    ruby-dev \
    zlib1g-dev

ADD . /usr/src/pipeline2
WORKDIR /usr/src/pipeline2
RUN if ! make dist-zip-linux; then \
      if [ -e .make-target/commands ]; then \
        echo "cat .make-target/commands" && \
        cat .make-target/commands | sed 's/^/> /g'; \
      fi && \
      if [ -e maven.log ]; then \
        echo "cat maven.log" && \
        cat maven.log | sed 's/^/> /g'; \
      fi && \
      exit 1; \
    fi
RUN cd assembly/target && unzip assembly-*-linux.zip
RUN make -C assembly src/main/docker/OpenJDK11-jdk_x64_linux_hotspot_11_28.tar.gz
RUN tar -zxvf assembly/src/main/docker/OpenJDK11-jdk_x64_linux_hotspot_11_28.tar.gz -C assembly/target/

# then use the build artifacts to create an image where the pipeline is installed
FROM debian:stretch
LABEL maintainer="Christian Egli <christian.egli@sbs.ch>"
COPY --from=builder /usr/src/pipeline2/assembly/target/daisy-pipeline /opt/daisy-pipeline2
COPY --from=builder /usr/src/pipeline2/assembly/target/jdk-11+28 /opt/jdk-11+28
ENV JAVA_HOME=/opt/jdk-11+28
ENV PIPELINE2_WS_LOCALFS=false \
    PIPELINE2_WS_AUTHENTICATION=true \
    PIPELINE2_WS_AUTHENTICATION_CLIENTKEY=clientid \
    PIPELINE2_WS_AUTHENTICATION_CLIENTSECRET=sekret
EXPOSE 8181
# for the healthcheck use PIPELINE2_HOST if defined. Otherwise use localhost
HEALTHCHECK --interval=30s --timeout=10s --start-period=1m CMD curl --fail http://${PIPELINE2_WS_HOST-localhost}:${PIPELINE2_WS_PORT:-8181}/${PIPELINE2_WS_PATH:-ws}/alive || exit 1
ENTRYPOINT ["/opt/daisy-pipeline2/bin/pipeline2"]
