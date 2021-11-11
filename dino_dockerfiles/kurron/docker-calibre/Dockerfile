FROM python:latest

MAINTAINER Ron Kurr <kurr@kurron.org>

LABEL org.kurron.ide.name="Calibre" org.kurron.ide.version=2.47.0 

ENV DEBIAN_FRONTEND noninteractive

ENV LANG C.UTF-8

RUN apt-get update && \
    apt-get install -y xvfb imagemagick && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

#RUN pip install --upgrade pip dnspython python-dateutil

# Create a user and group that matches what is in most Vagrant boxes
RUN groupadd --gid 1000 developer && \
    useradd --gid 1000 --uid 1000 --create-home --shell /bin/bash developer && \
    chown -R developer:developer /home/developer

ENV HOME /home/developer

VOLUME ["/home/developer"]

# where to store the database files
VOLUME ["/library"]

# where to import books from
VOLUME ["/import"]

ADD http://download.calibre-ebook.com/2.47.0/calibre-2.47.0-x86_64.txz /tmp/calibre-tarball.txz

RUN mkdir -p /opt/calibre && \
    rm -rf /opt/calibre/*  && \
    tar xvf /tmp/calibre-tarball.txz -C /opt/calibre && \
    /opt/calibre/calibre_postinstall && \
    mkdir -p /library && \
    mkdir -p /import 

EXPOSE 8080

USER developer:developer
WORKDIR /home/developer
ENTRYPOINT ["/usr/bin/calibre-server", "--with-library=/library"]
