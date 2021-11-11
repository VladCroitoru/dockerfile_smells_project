FROM openjdk:13
LABEL maintainer="mario.siegenthaler@linkyard.ch"

ENV SBT_VERSION 1.3.8


# add deps
# - libatomic: needed by protoc
# - git: needed by sbt when we use source dependency
RUN yum install -y -q libatomic git

RUN curl -sL https://github.com/sbt/sbt/releases/download/v1.3.8/sbt-1.3.8.tgz | \
    tar -xz -C /usr/local

RUN useradd --create-home -s /bin/bash scala

ENV SBT_HOME /usr/local/sbt
ENV PATH ${PATH}:${SBT_HOME}/bin

# This will build the compiler interface (which is really slow)
# - for Scala 2.13
COPY init_scala-2.13 /tmp/init
RUN cd /tmp/init && \
    sbt test && \
    rm -rf /tmp/init

#Run sbt once to initialize it along with commonly used dependencies
# = We trade a bigger image size against faster builds
COPY init_deps /tmp/init
RUN cd /tmp/init && \
    sbt test && \
    rm -rf /tmp/init


VOLUME /app
WORKDIR /app

CMD ["sbt"]
