FROM gliderlabs/logspout:master

COPY ./build-custom.sh /src/
COPY ./glide.yaml /src/
RUN cd /src && ./build-custom.sh "$(cat VERSION)-custom"

ENV ROUTE_URIS kinesis://kinesis-stream-name
