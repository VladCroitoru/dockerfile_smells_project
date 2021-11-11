FROM openjdk:8

MAINTAINER David Pollak <funcmaster-d@funcatron.org>

RUN \
    mkdir app && \
    git clone https://github.com/funcatron/tron.git && \
    wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein && \
    chmod +x lein && \
    mv lein /usr/local/bin && \
    cd tron && \
    git checkout stable && \
    export LEIN_ROOT=ok && \
    lein uberjar && \
    cp target/uberjar/tron-*-standalone.jar /tron.jar && \
    cd / && \
    rm -rf app && \
    rm -rf ~/.m2

EXPOSE 3000 54657

ENTRYPOINT ["/usr/bin/java", "-jar", "/tron.jar"]
