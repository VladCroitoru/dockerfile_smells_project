ARG DOCKER_REGISTRY=docker.io
ARG FROM_IMG_REPO=qnib
ARG FROM_IMG_NAME="alplain-openjdk8"
ARG FROM_IMG_TAG="2019-01-28.1"
ARG FROM_IMG_HASH=""
FROM ${DOCKER_REGISTRY}/${FROM_IMG_REPO}/${FROM_IMG_NAME}:${FROM_IMG_TAG}${DOCKER_IMG_HASH}

ARG MAVEN_VERSION="3.6.1"
ARG ZKUI_COMMIT=8d3441d0e3f2299a003d0d75308519e82564836c
LABEL zkui.commit=${ZKUI_COMMIT} \
      zkui.maven.version=${MAVEN_VERSION}
ENV ENTRYPOINTS_DIR=/opt/qnib/entry \
    M2_HOME=/usr/lib/mvn \
    ZKUI_PORT=9090 \
    ZK_SERVER=tasks.zookeeper:2181 \
    ZKUI_ADMIN_PW=manager \
    ZKUI_USER_PW=user
RUN apk --no-cache add wget curl libarchive-tools \
 && wget -qO - "http://ftp.unicamp.br/pub/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz" | tar xfz - -C /opt/ \
 && mv "/opt/apache-maven-$MAVEN_VERSION" "$M2_HOME" \
 && ln -s "$M2_HOME/bin/mvn" /usr/bin/mvn \
 && wget -qO - https://github.com/DeemOpen/zkui/archive/${ZKUI_COMMIT}.zip |bsdtar xf - -C /opt/ \
 && mv /opt/zkui-${ZKUI_COMMIT} /opt/zkui \
 && apk --no-cache del wget libarchive-tools \
 && cd /opt/zkui && mvn clean install \
 && rm -rf /tmp/* /var/cache/apk/* /usr/lib/mvn /opt/zkui/config.cfg
RUN echo "grep zkSer /opt/zkui/config.cfg" >> /root/.bash_history
COPY opt/qnib/zkui/bin/start.sh /opt/qnib/zkui/bin/
COPY opt/qnib/entry/* /opt/qnib/entry/
COPY opt/qnib/zkui/conf/zkui.conf.orig /opt/qnib/zkui/conf/
HEALTHCHECK --interval=2s --retries=30 --timeout=1s \
  CMD curl -sI http://127.0.0.1:${ZKUI_PORT}
CMD ["/opt/qnib/zkui/bin/start.sh"]
