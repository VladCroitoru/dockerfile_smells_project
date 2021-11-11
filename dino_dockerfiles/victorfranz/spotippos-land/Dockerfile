# URL: https://github.com/victorfranz/spotippos-land
#
# Reference:
#    - https://github.com/William-Yeh/docker-spray-httpserver
#
# Version 0.1
#

# pull base image
FROM williamyeh/scala:2.11.4
MAINTAINER Victor Franzonatto <victor.franzonatto@gmail.com>

ENV _JAVA_OPTIONS "-Dfile.encoding=UTF8"

RUN apt-get update  && \
    echo "==> Install git & helper tools..."  && \
    DEBIAN_FRONTEND=noninteractive \
        apt-get install -y -q --no-install-recommends git  && \
    \
    \
    \
    echo "==> Download source..."  && \
    cd /tmp  && \
    git clone https://github.com/victorfranz/spotippos-land.git  && \
    cd spotippos-land  && \
    \
    \
    echo "==> Compile & package..."  && \
    sbt assembly  && \
    mv target/scala-2.11/spotippos-land-0.1.jar /opt/spotippos-land.jar  && \
    \
    \
    \
    echo "==> Clean up..."  && \
    cd /tmp  && \
    rm -rf spotippos-land  && \
    apt-get remove -y --auto-remove git  && \
    apt-get clean  && \
    rm -rf /var/lib/apt/lists/*


# configure

# HTTP port
EXPOSE 8080

# for convenience
RUN date '+%Y-%m-%dT%H:%M:%S%:z' > /var/log/DOCKER_BUILD_TIME


# Define default command.
ENTRYPOINT ["java", "-jar", "/opt/spotippos-land.jar"]
CMD ["-XX:+UseG1GC"]
