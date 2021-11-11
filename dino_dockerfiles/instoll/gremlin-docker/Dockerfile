FROM openjdk:8-alpine

ENV VERSION 3.3.0
ENV CONSOLE_URL https://archive.apache.org/dist/tinkerpop/$VERSION/apache-tinkerpop-gremlin-console-$VERSION-bin.zip
ENV SERVER_URL  https://archive.apache.org/dist/tinkerpop/$VERSION/apache-tinkerpop-gremlin-server-$VERSION-bin.zip
ENV DIR gremlin

WORKDIR /gremlin

RUN echo "Installing dependencies.." && \
    apk update && \
    apk add wget unzip git bash && \
    echo "Downloading server.." && \
    wget --quiet -O /$DIR.zip $SERVER_URL && \
    unzip /$DIR.zip -d /$DIR && \
    rm /$DIR.zip && \
    echo "Setting up data dir.." && \
    mkdir /graph_file && \
    echo "Downloading console.." && \
    wget --quiet -O /$DIR.zip $CONSOLE_URL && \
    unzip /$DIR.zip -d /$DIR && \
    rm /$DIR.zip && \
    ln -s /gremlin/apache-tinkerpop-gremlin-console-$VERSION/bin/gremlin.sh /usr/bin/gremlin-console

WORKDIR /gremlin/apache-tinkerpop-gremlin-server-$VERSION

COPY files  .
COPY run.sh .

CMD ["./run.sh"]
