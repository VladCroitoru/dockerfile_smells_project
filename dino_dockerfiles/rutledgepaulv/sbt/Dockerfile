FROM frolvlad/alpine-oraclejdk8
MAINTAINER paul.v.rutledge@gmail.com

ENV SBT_VERSION 0.13.9
ENV SCALA_VERSION 2.11.7
ENV SCALA_HOME /usr/local/share/scala
RUN export PATH=$PATH:${SCALA_HOME}/bin


RUN wget http://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz && \
    wget http://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-launch/${SBT_VERSION}/sbt-launch.jar && \
    mkdir -p ~/bin && touch ~/bin/sbt && \
    echo '#!/bin/sh' | tee -a ~/bin/sbt && \
    echo 'SBT_OPTS="-Xms512M -Xmx1536M -Xss1M -XX:+CMSClassUnloadingEnabled"' | tee -a ~/bin/sbt && \
    echo 'java $SBT_OPTS -jar /sbt-launch.jar "$@"' | tee -a ~/bin/sbt && \
    chmod +x ~/bin/sbt && \
    ln -s ~/bin/sbt /usr/local/bin/sbt && \
    tar xvzf scala-${SCALA_VERSION}.tgz && \
    mv scala-${SCALA_VERSION} ${SCALA_HOME} && \
    rm -f scala-${SCALA_VERSION}.tgz

# compile a non-existent project to pre-download sbt dependencies
RUN sbt compile

CMD ["sbt"]