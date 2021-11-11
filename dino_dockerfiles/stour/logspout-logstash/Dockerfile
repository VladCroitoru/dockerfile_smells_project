FROM stour/logspout:latest

ENV DOCKERIZE_VERSION v0.2.0
COPY dockerize-linux-amd64-v0.2.0.tar.gz /
RUN tar -C /usr/local/bin -xzvf /dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm /dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
