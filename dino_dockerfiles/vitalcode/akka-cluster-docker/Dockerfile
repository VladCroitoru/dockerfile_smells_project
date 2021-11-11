FROM hseeberger/scala-sbt
MAINTAINER vitalcode

ADD . /data
WORKDIR /data
RUN sbt clean docker:stage

EXPOSE 2551

ENTRYPOINT ["target/docker/stage/opt/docker/bin/akka-cluster-docker"]
CMD []

