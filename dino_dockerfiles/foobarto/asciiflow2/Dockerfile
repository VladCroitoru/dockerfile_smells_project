FROM nginx:stable-alpine
ADD . /etc/nginx/html
WORKDIR /etc/nginx/html

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/jre
ENV PATH $PATH:$JAVA_HOME/bin

ENV JAVA_VERSION 8u77
ENV JAVA_ALPINE_VERSION 8.77.03-r0

RUN set -x \
    && apk add --no-cache \
      openjdk8-jre="$JAVA_ALPINE_VERSION" \
    && chmod u+x closure-compiler.jar \
    && ./compile.sh \
    && rm closure-compiler.jar compile.sh \
    && apk del openjdk8-jre
