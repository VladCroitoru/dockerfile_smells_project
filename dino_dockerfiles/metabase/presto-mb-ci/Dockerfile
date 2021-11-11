FROM openjdk:8

MAINTAINER Jeff Evans <jeff.evans@metabase.com>

ENV PRESTO_VERSION 0.254

RUN mkdir /opt/presto && \
    curl -LS https://repo1.maven.org/maven2/com/facebook/presto/presto-server/${PRESTO_VERSION}/presto-server-${PRESTO_VERSION}.tar.gz | tar -xz --strip-components=1 -C /opt/presto

RUN curl -Lo /usr/local/bin/presto https://repo1.maven.org/maven2/com/facebook/presto/presto-cli/${PRESTO_VERSION}/presto-cli-${PRESTO_VERSION}-executable.jar && \
    chmod +x /usr/local/bin/presto

COPY ["./etc", "/opt/presto/etc"]

RUN keytool \
        -genkeypair \
        -alias "presto" \
        -keyalg RSA \
        -keystore /opt/presto/etc/keystore.jks \
        -validity 10000 \
        -dname "CN=*.presto-ci.metabase.com, OU=Engineering, O=Metabase, L=San Francisco, S=CA, C=USA" \
        -ext "SAN:c=DNS:localhost,IP:127.0.0.1,DNS:presto" \
        -storepass metabase

EXPOSE 8080 8443

CMD ["/opt/presto/bin/launcher", "run"]
