FROM anapsix/alpine-java:jdk8

RUN wget -O - http://dl.bintray.com/sbt/native-packages/sbt/0.13.12/sbt-0.13.12.tgz \
    | gunzip \
    | tar -x -C /usr/local

ENV PATH="/usr/local/sbt/bin:${PATH}"

RUN sbt
