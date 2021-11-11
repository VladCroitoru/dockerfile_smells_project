FROM ubuntu:xenial

ENV INTELLIJ_VERSION 2017.3

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl openjdk-8-jdk && \
    apt-get clean all && \
    mkdir /home/intellij && \
    useradd intellij -d /home/intellij && \
    curl http://download-cf.jetbrains.com/idea/ideaIC-${INTELLIJ_VERSION}.tar.gz > /home/intellij/ideaIC-${INTELLIJ_VERSION}.tar.gz && \
    chown -R intellij:intellij /home/intellij && \
    cd /home/intellij && \
    tar xvzf ideaIC-${INTELLIJ_VERSION}.tar.gz && \
    rm -f ideaIC-${INTELLIJ_VERSION}.tar.gz && \
    mv /home/intellij/idea* /home/intellij/idea

USER intellij

ENTRYPOINT [ "/home/intellij/idea/bin/idea.sh" ]
