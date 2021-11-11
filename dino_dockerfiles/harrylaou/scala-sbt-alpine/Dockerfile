FROM  frolvlad/alpine-scala
LABEL maintainer="harry@talos.software"
ENV SCALA_VERSION=2.13.4 \
  SBT_VERSION=1.4.6

RUN \
  echo "$SCALA_VERSION $SBT_VERSION" && \
  apk add --no-cache bash curl bc ca-certificates && \
  update-ca-certificates && \
  scala -version && \
  scalac -version && \
  curl -fsL https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz | tar xfz - -C /usr/local && \
  $(mv /usr/local/sbt-launcher-packaging-$SBT_VERSION /usr/local/sbt || true) && \
  ln -s /usr/local/sbt/bin/* /usr/local/bin/ && \
  apk del curl && \
  sbt -Dsbt.rootdir=true sbtVersion
