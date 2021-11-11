FROM ubuntu:14.04

# Get some basics installed
RUN apt-get update \
    && apt-get install -qqy openjdk-6-jdk \
    && apt-get install -qqy wget \
    && apt-get install -qqy dpkg

# Install scala
RUN wget http://www.scala-lang.org/files/archive/scala-2.11.4.deb \
    && dpkg -i scala-2.11.4.deb \
    && apt-get update \
    && apt-get install -qqy scala

# Install sbt
RUN echo "deb http://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list \
    && apt-get update \
    && apt-get install -qqy --force-yes sbt

# Get scalding
RUN apt-get update && apt-get install -qqy git \
    && git clone https://github.com/twitter/scalding.git

# Help Java fork processes better (https://groups.google.com/forum/#!msg/spark-users/_jEBtcxNLEk/ZgVUqqksvegJ)
RUN echo "vm.overcommit_memory = 1" >> /etc/sysctl.conf

WORKDIR /scalding

# Warm up the repl
RUN sbt scalding-repl/compile
RUN mkdir /src
ENTRYPOINT ["sbt", "scalding-repl/console"]
