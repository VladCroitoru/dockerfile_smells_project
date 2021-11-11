FROM ubuntu:xenial
MAINTAINER Neblio <info@nebl.io>

COPY --from=neblioteam/nebliod:latest /root/.neblio.bootstrapped /root/.neblio.bootstrapped

ADD ./bin /usr/local/bin
RUN chmod 755 /usr/local/bin/neblio_quicksync_copy

VOLUME /root/.neblio

CMD ["neblio_quicksync_copy"]