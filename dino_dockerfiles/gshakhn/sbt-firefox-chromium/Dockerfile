FROM java:jdk-alpine
MAINTAINER George Shakhnazaryan

ENV CHROMIUM_VERSION=49.0.2623.110-r1
ENV FIREFOX_VERSION=45.2.0-r0
ENV SBT_VERSION=0.13.11

RUN apk --no-cache add \
  bash \
  curl \
  chromium=$CHROMIUM_VERSION \
  dbus \
  firefox-esr=$FIREFOX_VERSION \
  libexif \
  ttf-freefont \
  udev \
  xvfb

RUN dbus-uuidgen > /var/lib/dbus/machine-id

RUN mkdir /opt
WORKDIR /opt
RUN curl -SL https://dl.bintray.com/sbt/native-packages/sbt/${SBT_VERSION}/sbt-${SBT_VERSION}.tgz | tar xz
COPY sbt-with-xvfb.sh .

WORKDIR /app

VOLUME ["/app", "/cache/.sbt", "/cache/.ivy2"]

ENTRYPOINT ["/opt/sbt-with-xvfb.sh"]
