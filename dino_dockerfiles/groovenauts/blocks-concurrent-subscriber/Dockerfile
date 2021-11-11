FROM debian:jessie

ARG version=0.2.1

RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates && \
    apt-get clean

ADD https://github.com/groovenauts/blocks-concurrent-subscriber/releases/download/${version}/blocks-concurrent-subscriber_linux_amd64 \
    /blocks-concurrent-subscriber

RUN chmod +x /blocks-concurrent-subscriber

CMD /blocks-concurrent-subscriber
