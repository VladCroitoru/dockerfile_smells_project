FROM clojure:openjdk-17-lein-alpine

WORKDIR /usr/src/app

RUN apk add --no-cache git

CMD ["--help"]

RUN mkdir -p /etc/iplant/de/crypto && \
    touch /etc/iplant/de/crypto/pubring.gpg && \
    touch /etc/iplant/de/crypto/random_seed && \
    touch /etc/iplant/de/crypto/secring.gpg && \
    touch /etc/iplant/de/crypto/trustdb.gpg

COPY conf/main/logback.xml /usr/src/app/

COPY project.clj /usr/src/app/
RUN lein deps

RUN ln -s "/opt/openjdk-17/bin/java" "/bin/terrain"

COPY . /usr/src/app

RUN lein do clean, uberjar && \
    cp target/terrain-standalone.jar .

# Add the Internet2 InCommon intermediate CA certificate.
ADD "https://incommon.org/wp-content/uploads/2019/06/sha384-Intermediate-cert.txt" "/usr/local/share/ca-certificates/"
RUN sed -i -E 's/\r\n?/\n/g' "/usr/local/share/ca-certificates/sha384-Intermediate-cert.txt" && \
    update-ca-certificates

ENTRYPOINT ["terrain", "-Dlogback.confonFile=/etc/iplant/de/logging/terrain-logging.xml", "-cp", ".:terrain-standalone.jar", "terrain.core"]

ARG git_commit=unknown
ARG version=unknown
ARG descriptive_version=unknown

LABEL org.cyverse.git-ref="$git_commit"
LABEL org.cyverse.version="$version"
LABEL org.cyverse.descriptive-version="$descriptive_version"
LABEL org.opencontainers.image.authors="CyVerse Core Software Team <support@cyverse.org>"
LABEL org.opencontainers.image.revision="$git_commit"
LABEL org.opencontainers.image.source="https://github.com/cyverse-de/terrain"
LABEL org.opencontainers.image.version="$descriptive_version"
