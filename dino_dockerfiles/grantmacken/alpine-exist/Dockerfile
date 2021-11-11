FROM  openjdk:8-jre-alpine3.8 as maker
# exposes java in $PATH
# and following ENV
# JAVA_HOME
ARG VERSION=4.3.1
ENV VERSION=$VERSION
LABEL maintainer="Grant Mackenzie <grantmacken@gmail.com>" \
      org.label-schema.build-date="$(date --iso)" \
      org.label-schema.vcs-ref="$(git rev-parse --short HEAD)" \
      org.label-schema.vcs-url="https://github.com/grantmacken/alpine-eXist" \
      org.label-schema.schema-version="1.0"

WORKDIR /home

COPY .env .env
COPY eXist.expect eXist.expect

RUN echo "Build eXist version: ${VERSION}" \
 && wget -q -O eXist-db-setup.jar \
 https://bintray.com/artifact/download/existdb/releases/eXist-db-setup-${VERSION}.jar \
  && apk add --no-cache --virtual .build-deps expect \
  && export $(xargs <.env) \
  && chmod +x eXist.expect \
  && ./eXist.expect \
  && rm eXist-db-setup.jar \
  && apk del .build-deps

ENV EXIST_HOME  "/usr/local/eXist"
WORKDIR /home/eXist

RUN rm -rv \
  bin \
  build \
  extensions/debuggee \
  extensions/exiftool \
  extensions/metadata \
  extensions/netedit \
  extensions/security \
  extensions/tomcat-realm \
  extensions/xprocxq \
  installer \
  samples \
  src \
  test \
  tools/Solaris \
  tools/appbundler \
  tools/jetty/etc/standalone \
  tools/jetty/standalone-webapps \
  tools/jetty/webapps/portal \
  tools/rulesets \
  tools/yajsw \
  && rm -f \
  lib/extensions/exiftool.jar \
  lib/extensions/exist-security-* \
  lib/extensions/xprocxq.jar \
  tools/jetty/etc/standalone* \
  webapp/WEB-INF/*.tmpl \
  && echo ' - select only stuff required to run eXist' \
  && mkdir -p $EXIST_HOME \
  && echo ' - copy sundries' \
  && for i in \
  'LICENSE' \
  'client.properties'; \
  do cp $i $EXIST_HOME; done\
  && ls -al $EXIST_HOME \
  && echo ' - copy base folders' \
  && cp -r autodeploy $EXIST_HOME \
  && echo ' - copy base libs' \
  && for i in \
  'exist-optional.jar'\
  'exist.jar' \
  'start.jar'; \
  do cp $i $EXIST_HOME; done \
  && mkdir $EXIST_HOME/lib \
  && for i in \
  'lib/core' \
  'lib/endorsed' \
  'lib/extensions' \
  'lib/optional' \
  'lib/test' \
  'lib/user'; \
  do cp -r $i $EXIST_HOME/lib  ; done \
  && echo ' - symlink root config files' \
  && mkdir $EXIST_HOME/config \
  && for i in \
  'conf.xml'\
  'descriptor.xml' \
  'log4j2.xml' \
  'mime-types.xml'; \
  do mv $i $EXIST_HOME/config;\
  ln -s -v -T $EXIST_HOME/config/$i $EXIST_HOME/$i; done \
  && echo ' - copy tools' \
  && mkdir $EXIST_HOME/tools \
  && for i in \
  'tools/ant' \
  'tools/aspectj' \
  'tools/jetty'; \
  do cp -r $i $EXIST_HOME/tools; done \
  && echo ' - copy extension libs' \
  && mkdir -p $EXIST_HOME/extensions/exquery/restxq \
  && mkdir -p $EXIST_HOME/extensions/betterform/main \
  && mkdir -p $EXIST_HOME/extensions/contentextraction \
  && mkdir -p $EXIST_HOME/extensions/expath \
  && mkdir -p $EXIST_HOME/extensions/indexes/lucene \
  && mkdir -p $EXIST_HOME/extensions/modules \
  && mkdir -p $EXIST_HOME/extensions/webdav \
  && mkdir -p $EXIST_HOME/extensions/xqdoc \
  && cp -r extensions/betterform/main/lib $EXIST_HOME/extensions/betterform/main \
  && cp -r extensions/contentextraction/lib $EXIST_HOME/extensions/contentextraction \
  && cp -r extensions/expath/lib $EXIST_HOME/extensions/expath \
  && cp -r extensions/exquery/lib $EXIST_HOME/extensions/exquery \
  && cp -r extensions/exquery/restxq/lib $EXIST_HOME/extensions/exquery/restxq \
  && cp -r extensions/indexes/lucene/lib $EXIST_HOME/extensions/indexes/lucene \
  && cp -r extensions/modules/lib  $EXIST_HOME/extensions/modules \
  && cp -r extensions/webdav/lib $EXIST_HOME/extensions/webdav \
  && cp -r extensions/xqdoc/lib $EXIST_HOME/extensions/xqdoc \
  && echo ' - copy webapp' \
  && cp -r webapp  $EXIST_HOME \
  && echo ' - move and symlink webapp config files' \
  && mv $EXIST_HOME/tools/jetty/webapps/exist-webapp-context.xml $EXIST_HOME/config \
  && ln -s -v -T \
  $EXIST_HOME/config/exist-webapp-context.xml \
  $EXIST_HOME/tools/jetty/webapps/exist-webapp-context.xml \
  && echo 'move and symlink jetty config files' \
  && mv $EXIST_HOME/webapp/WEB-INF/controller-config.xml $EXIST_HOME/config \
  && ln -s -v -T \
  $EXIST_HOME/config/controller-config.xml \
  $EXIST_HOME/webapp/WEB-INF/controller-config.xml \
  && rm -r /home/*

FROM openjdk:8-jre-alpine3.8 as base

COPY --from=maker /usr/local/eXist /usr/local/eXist
RUN  echo ' - remove  stuff from jre' \
    && cd /usr/lib/jvm/java-1.8-openjdk/bin \
    && rm -rv orbd pack200 rmid rmiregistry servertool tnameserv unpack200 \
    && cd /usr/lib/jvm/java-1.8-openjdk/jre/lib/ext \
    && rm -v nashorn.jar

ENV LANG C.UTF-8
ENV EXIST_HOME /usr/local/eXist
EXPOSE 8080
WORKDIR $EXIST_HOME
ENTRYPOINT ["java", "-Djava.awt.headless=true", "-jar", "start.jar", "jetty"]
