FROM clojure:lein-2.6.1-alpine

ADD . /opt/build

RUN cd /opt/build && \
    lein cljsbuild once prod && \
    lein uberjar && \
    cp target/chronojob-0.1.0-SNAPSHOT-standalone.jar /opt/ && \
    cp config/prod.clj /opt/config.clj && \
    cp config/logback_prod.xml /opt/logback.xml && \
    cd / && \
    rm -rf /opt/build

EXPOSE 7000

CMD /usr/bin/java -cp /opt/:/opt/chronojob-0.1.0-SNAPSHOT-standalone.jar chronojob.core /opt/config.clj
