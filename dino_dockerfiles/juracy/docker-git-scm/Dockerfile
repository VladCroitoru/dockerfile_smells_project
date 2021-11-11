FROM debian:8.6
MAINTAINER Juracy Filho <juracy@gmail.com>

ENV GIT_URL=https://www.kernel.org/pub/software/scm/git
ENV GIT_VERSION=2.11.0
ENV GIT_FILENAME=git-${GIT_VERSION}
ENV GIT_ARCHIVE=${GIT_FILENAME}.tar.gz
ENV GIT_MANPAGES=git-manpages-${GIT_VERSION}.tar.gz

RUN mkdir /work && \
    apt-get update && \
    apt-get install -y wget build-essential libssl-dev libcurl4-gnutls-dev gettext expat libexpat1-dev zlib1g-dev man python && \
    cd /tmp && \
    wget ${GIT_URL}/${GIT_ARCHIVE} && \
    wget ${GIT_URL}/${GIT_MANPAGES} && \
    tar xfz ${GIT_ARCHIVE} && \
    cd ${GIT_FILENAME} && \
    make -j4 prefix=/usr all && \
    make prefix=/usr install && \
    cd /usr/share/man && \
    tar xfz /tmp/${GIT_MANPAGES} && \
    mandb && \
    cd /tmp && \
    rm -rf ${GIT_FILENAME} && \
    rm ${GIT_MANPAGES} && \
    rm ${GIT_ARCHIVE} && \
    apt-get remove -y wget build-essential libssl-dev libcurl4-gnutls-dev gettext expat libexpat1-dev zlib1g-dev python && \
    apt-get autoremove -y

WORKDIR /work
CMD ["/bin/bash"]
