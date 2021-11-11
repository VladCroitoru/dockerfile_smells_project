FROM debian:jessie

RUN apt-get update && apt-get install -y build-essential curl libpurple-dev libjson-glib-dev libglib2.0-dev libprotobuf-c-dev protobuf-c-compiler mercurial make

# nightly bitlbee
RUN echo 'deb http://code.bitlbee.org/debian/master/jessie/amd64/ ./' > /etc/apt/sources.list.d/bitlbee.list && \
    curl https://code.bitlbee.org/debian/release.key | apt-key add -

# nightly bitlbee-facebook
RUN echo 'deb http://download.opensuse.org/repositories/home:/jgeboski/Debian_8.0 ./' > /etc/apt/sources.list.d/jgeboski.list && \
    curl https://jgeboski.github.io/obs.key | apt-key add -

RUN apt-get update && \
    apt-get install -y bitlbee && \
    apt-get install -y bitlbee-facebook && \
    apt-get install -y bitlbee-libpurple

# add google hangouts to libpurple
RUN hg clone https://bitbucket.org/EionRobb/purple-hangouts/ && cd purple-hangouts && make && make install

VOLUME "/var/lib/bitlbee"

EXPOSE 6667
CMD ["/usr/sbin/bitlbee", "-F", "-n"] # -F is ForkDaemon mode, required for libpurple
