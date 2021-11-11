FROM centos:7
MAINTAINER ryotas

RUN echo "#!/bin/sh" > hellogalaxy && \
    echo "echo 'Hello Galaxy'" >> hellogalaxy && \
    chmod +x hellogalaxy && \
    cp hellogalaxy /usr/local/bin/
