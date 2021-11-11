FROM discoenv/clojure-base:master

ENV CONF_TEMPLATE=/usr/src/app/terrain.properties.tmpl
ENV CONF_FILENAME=terrain.properties
ENV PROGRAM=terrain

RUN mkdir -p /etc/iplant/de/crypto && \
    touch /etc/iplant/de/crypto/pubring.gpg && \
    touch /etc/iplant/de/crypto/random_seed && \
    touch /etc/iplant/de/crypto/secring.gpg && \
    touch /etc/iplant/de/crypto/trustdb.gpg

VOLUME ["/etc/iplant/de"]

COPY project.clj /usr/src/app/
RUN lein deps

COPY conf/main/logback.xml /usr/src/app/
COPY . /usr/src/app

RUN lein uberjar && \
    cp target/terrain-standalone.jar .

RUN ln -s "/usr/bin/java" "/bin/terrain"

ENTRYPOINT ["run-service", "-Dlogback.configurationFile=/etc/iplant/de/logging/terrain-logging.xml", "-cp", ".:terrain-standalone.jar", "terrain.core"]
CMD ["--help"]

ARG git_commit=unknown
ARG version=unknown
ARG descriptive_version=unknown

LABEL org.cyverse.git-ref="$git_commit"
LABEL org.cyverse.version="$version"
LABEL org.cyverse.descriptive-version="$descriptive_version"
LABEL org.label-schema.vcs-ref="$git_commit"
LABEL org.label-schema.vcs-url="https://github.com/cyverse-de/terrain"
LABEL org.label-schema.version="$descriptive_version"
