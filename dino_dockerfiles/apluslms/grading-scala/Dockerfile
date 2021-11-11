ARG BASE_TAG=latest
FROM apluslms/grade-java:$BASE_TAG

ARG SCALA_VER=2.13
ARG SCALA_FVER=2.13.6
ARG SCALA_URL=https://downloads.lightbend.com/scala/$SCALA_FVER/scala-$SCALA_FVER.tgz
ARG SCALA_DIR=/usr/local/scala
ENV SCALA_HOME=$SCALA_DIR/scala-$SCALA_FVER

RUN mkdir -p $SCALA_HOME && cd $SCALA_HOME  \
\
 # Download scala scripts
 # TODO: move scala script into our own repo or recreate it
 && curl -LSs $SCALA_URL -o - \
  | tar zx --strip-components=1 \
     scala-$SCALA_FVER/bin/scala \
     scala-$SCALA_FVER/bin/scalac \
 && ln -s $SCALA_HOME/bin/scala \
          $SCALA_HOME/bin/scalac \
          /usr/local/bin \
\
 # Download libraries
 && ivy_install -n "scala-library" -d "$SCALA_HOME/lib" \
    # These go to boot classpath
    # core
    org.scala-lang scala-library $SCALA_FVER \
    # compiler
    org.scala-lang scala-compiler $SCALA_FVER \
    org.scala-lang.modules scala-parser-combinators_$SCALA_VER 1.1.2 \
 && ivy_install -n "grade-scala" -d "$SCALA_DIR/lib" \
    # These go to classpath
    # core libs are repeated, so the deps are resolved to same jars
    org.scala-lang scala-library $SCALA_FVER \
    org.scala-lang scala-compiler $SCALA_FVER \
    # extra libs
    org.scala-lang.modules scala-swing_$SCALA_VER 2.1.1 \
    # for grading
    org.scalatest scalatest_$SCALA_VER 3.2.5 "default->master,compile,runtime" \
    org.scalamock scalamock_$SCALA_VER 5.1.0 \
    com.beautiful-scala scalastyle_$SCALA_VER [1.5.0,1.6[ \
    com.typesafe.akka akka-actor_$SCALA_VER [2.6.14,2.7[ \
 && :

# Add scala utilities
COPY bin /usr/local/bin

ENV CLASSPATH=.:/exercise:/exercise/*:/exercise/lib/*:$SCALA_DIR/lib/*:/usr/local/java/lib/*
