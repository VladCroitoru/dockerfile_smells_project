FROM ubuntu:14.04

RUN set -x         && \
    apt-get update && \
    apt-get clean

RUN set -x                                                             && \
    apt-get install -y openssl libcurl4-openssl-dev libxml2 libssl-dev    \
                       libxml2-dev pinentry-curses curl make unzip     && \
    apt-get clean

RUN apt-get install -y gettext-base gawk

ENV VER 1.0.0

RUN set -x                                                                && \
    curl -OL https://github.com/lastpass/lastpass-cli/archive/v${VER}.zip && \
    echo 2f68a6835eecea738cd6a141881c9f8f v${VER}.zip | md5sum -c -       && \
    unzip v${VER}.zip && rm v${VER}.zip                                   && \
    cd lastpass-cli-${VER}                                                && \
    make && make install                                                  && \
    cd / && rm -rf /lastpass-cli-${VER}

ADD bin/bash-askpass /usr/local/bin/bash-askpass
ADD bin/quiet-askpass /usr/local/bin/quiet-askpass

VOLUME /root/.lpass

ENTRYPOINT ["/usr/bin/lpass"]
