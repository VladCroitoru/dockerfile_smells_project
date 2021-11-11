FROM adoptopenjdk:11-jdk-hotspot

# Setup adapted from https://github.com/hseeberger/scala-sbt/blob/master/debian/Dockerfile
RUN \
  apt-get update -q && \
  apt-get upgrade -qq && \
  apt-get install -y git && \
  rm -rf /var/lib/apt/lists/*

# Any RUN command after an ARG is set has that value in it as an environment variable and thus
# invalidates layer cache, so only declaring these ARGs when they're used

ARG SBT_VERSION
RUN \
  curl -L "https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz" | tar zxf - -C /usr/share  && \
  cd /usr/share/sbt/bin && \
  rm sbt.bat sbtn-x86_64-apple-darwin sbtn-x86_64-pc-linux sbtn-x86_64-pc-win32.exe && \
  ln -s /usr/share/sbt/bin/sbt /usr/local/bin/sbt

ARG SCALA_VERSION
RUN \
  mkdir /setup-project && \
  cd /setup-project && \
  echo "scalaVersion := \"${SCALA_VERSION}\"" > build.sbt && \
  echo "case object Temp" > Temp.scala && \
  sbt compile && \
  rm -rf /setup-project

CMD ["bash"]
