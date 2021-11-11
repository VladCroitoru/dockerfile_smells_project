FROM centos:latest

ENV HOME=/opt/zeppelin \
    MAVEN_VERSION=3.3.9 \
    JAVA_HOME=/usr/lib/jvm/java \
    ZEPPELIN_VERSION=0.7.3 \
    ZEPPELIN_SERVER_HOME=/opt/zeppelin/server \
    ZEPPELIN_STORAGE_DIR=/opt/zeppelin/storage \
    ZEPPELIN_CONF_DIR=/opt/zeppelin/storage/conf \
    ZEPPELIN_LOG_DIR=/opt/zeppelin/storage/logs \
    ZEPPELIN_NOTEBOOK_DIR=/opt/zeppelin/storage/notebook \
    ZEPPELIN_INTERPRETER_DIR=/opt/zeppelin/storage/interpreter \
    ZEPPELIN_WAR_TEMPDIR=/opt/zeppelin/storage/webapps


RUN yum clean all && \
    export INSTALL_PKGS="java-1.8.0-openjdk-devel java-1.8.0-openjdk-headless gettext tar git which unzip" && \
    yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    yum clean all && \
    mkdir -p $HOME/server $HOME/bin $HOME/storage && \
    curl -fsSL http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \
      && mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
      && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn && \
    curl -fSL http://archive.apache.org/dist/zeppelin/zeppelin-$ZEPPELIN_VERSION/zeppelin-$ZEPPELIN_VERSION-bin-netinst.tgz | tar xzf - --strip 1 -C $ZEPPELIN_SERVER_HOME/ && \
    chown -R 1001:0 $HOME/server $HOME/bin $HOME/storage && \
    chmod -R "g+rwX" $HOME/server $HOME/bin $HOME/storage
    
ADD bin/start.sh $HOME/bin/

RUN chmod +x $HOME/bin/start.sh

EXPOSE 8080

WORKDIR $HOME

VOLUME /opt/zeppelin/storage

USER root

ENTRYPOINT ["/opt/zeppelin/bin/start.sh"]
