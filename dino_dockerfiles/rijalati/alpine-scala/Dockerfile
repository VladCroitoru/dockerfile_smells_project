FROM rijalati/alpine-zulu-jdk8:latest-mini
MAINTAINER <ritchie@selectstar.io>

RUN apk add --update --no-cache bash \
&& cd /opt \
&& curl -Ls https://downloads.lightbend.com/scala/2.12.1/scala-2.12.1.tgz \
| tar --strip-components=1 -xzvf -

ENTRYPOINT ["/opt/bin/scala", "-version"]
