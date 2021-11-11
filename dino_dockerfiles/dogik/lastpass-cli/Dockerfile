# Lastpass cli
#
# Usage:
# alias lpass="docker run -v $HOME/.lpass:/root/.lpass -v /etc/localtime:/etc/localtime -i -t --rm dogik/lastpass-cli"

FROM ubuntu
MAINTAINER Sergey Dogotar <sergey.dogotar@gmail.com>

RUN apt-get update -y && apt-get install --no-install-recommends -y -q git ca-certificates openssl libcurl4-openssl-dev libxml2 libssl-dev libxml2-dev pinentry-curses xclip cmake build-essential pkg-config

RUN git clone https://github.com/LastPass/lastpass-cli.git /usr/src/lastpass-cli

WORKDIR /usr/src/lastpass-cli

RUN make && make install

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/*

ENTRYPOINT ["lpass"]
