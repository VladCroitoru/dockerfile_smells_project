FROM kurron/docker-jetbrains-base:latest

MAINTAINER Ron Kurr <kurr@kurron.org>

LABEL org.kurron.ide.name="Emacs" org.kurron.ide.version=24.5


# Install make and compilers
RUN apt-get update && \
    apt-get install -y build-essential autoconf automake && \
    apt-get build-dep -y emacs24 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

ADD http://ftp.gnu.org/gnu/emacs/emacs-24.5.tar.gz /tmp/ide.tar.gz

RUN mkdir -p /opt/ide && \
    tar zxvf /tmp/ide.tar.gz --strip-components=1 -C /opt/ide && \
    rm /tmp/ide.tar.gz

WORKDIR /opt/ide
RUN ./configure && \
    make && \
    make install

USER developer:developer
WORKDIR /home/developer
ENTRYPOINT ["/usr/local/bin/emacs"]
