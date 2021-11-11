# SBT on Java 8
#
# URL: https://github.com/nightscape/docker-sbt
#
# forked from: William-Yeh/docker-scala
#              - https://index.docker.io/u/pulse00/scala/
#              - https://github.com/dubture-dockerfiles/scala
#
# Version     0.7

FROM jeanblanchard/busybox-java:8
MAINTAINER Martin Mauch <martin.mauch@gmail.com>

RUN opkg-install bash

ENV SBT_VERSION 0.13.8

RUN mkdir -p /usr/local/bin && wget -P /usr/local/bin/ http://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-launch/$SBT_VERSION/sbt-launch.jar && ls /usr/local/bin

COPY sbt /usr/local/bin/


# create an empty sbt project;
# then fetch all sbt jars from Maven repo so that your sbt will be ready to be used when you launch the image
COPY test-sbt.sh /tmp/

ENV SCALA_VERSION 2.11.6

RUN cd /tmp  && \
    mkdir -p src/main/scala && \
    echo "object Main {}" > src/main/scala/Main.scala && \
    ./test-sbt.sh  && \
    rm -rf *

# print versions
#RUN java -version

# scala -version returns code 1 instead of 0 thus "|| true"
#RUN scala -version || true



# Define default command.
CMD ["sbt"]
