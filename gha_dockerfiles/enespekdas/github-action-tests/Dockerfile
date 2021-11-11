FROM fedora:latest
LABEL maintainer Emre Özkan <emreozkan@windowslive.com>

RUN dnf install -y tar gzip gcc make \
        && dnf clean all

ADD http://ftpmirror.gnu.org/hello/hello-2.10.tar.gz /tmp/hello-2.10.tar.gz

RUN tar xvzf /tmp/hello-2.10.tar.gz -C /opt

WORKDIR /opt/hello-2.10

RUN ./configure
RUN make
RUN make install
RUN hello -v
ENTRYPOINT "/usr/local/bin/hello"