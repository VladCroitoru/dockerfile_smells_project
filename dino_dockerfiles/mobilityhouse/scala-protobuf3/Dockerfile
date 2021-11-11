FROM openjdk:8u102-jdk
MAINTAINER David Asabina <vid@bina.me>
RUN apt-get update && apt-get install -y \
      apt-transport-https \
  && echo "deb https://dl.bintray.com/sbt/debian /" | \
    tee -a /etc/apt/sources.list.d/sbt.list \
  && apt-key adv \
    --keyserver hkp://keyserver.ubuntu.com:80 \
    --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823 \
  && apt-get update \
  && apt-get install sbt
ADD bench /tmp/sbt-work-dir
WORKDIR /tmp/sbt-work-dir
RUN sbt reload
CMD sbt compile
