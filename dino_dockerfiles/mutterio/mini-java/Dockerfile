FROM mutterio/mini-base

ENV JAVA_VERSION 7.71.2.5.3-r1
ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk

RUN apk add --update openjdk7-jre-base \
  && rm -rf /var/cache/apk/* &&\
  find /usr/share/ca-certificates/mozilla/ -name *.crt -exec keytool -import -trustcacerts \
  -keystore /usr/lib/jvm/java-1.7-openjdk/jre/lib/security/cacerts -storepass changeit -noprompt \
  -file {} -alias {} \; && \
  keytool -list -keystore /usr/lib/jvm/java-1.7-openjdk/jre/lib/security/cacerts --storepass changeit

CMD ["/bin/sh"]
