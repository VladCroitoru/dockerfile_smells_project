#ARG OPENJDK_VERSION=12-alpine
ARG OPENJDK_VERSION=8-jre-alpine
FROM openjdk:${OPENJDK_VERSION}

LABEL maintainer="Ben Fortuna <fortuna@micronode.com>"

ARG SLING_VERSION=11

ENV BUNDLE_PATHS=/opt/sling/wp/install,/opt/sling/bundles
ENV JAVA_OPTS='-XX:MaxRAM=768m -Xmx384m -XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap'
ENV SLING_OPTS=''

RUN mkdir -p /opt/sling
RUN wget https://repo1.maven.org/maven2/org/apache/sling/org.apache.sling.starter/${SLING_VERSION}/org.apache.sling.starter-${SLING_VERSION}.jar -O /opt/sling/org.apache.sling.starter.jar

# sha1sum.txt must be updated when switching to a different jar,
# or docker build will fail
# COPY sha1sum.txt /tmp
# RUN sha1sum -c /tmp/sha1sum.txt

WORKDIR /opt/sling/
EXPOSE 8080
VOLUME /opt/sling/sling

CMD exec java -Dsling.fileinstall.dir=${BUNDLE_PATHS} ${JAVA_OPTS} -jar org.apache.sling.starter.jar $SLING_OPTS

HEALTHCHECK CMD wget -O- localhost:8080/system/health.txt?httpStatus=CRITICAL:503
