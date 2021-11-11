FROM alpine:latest
MAINTAINER Octoblu <docker@octoblu.com>

ENV XDG_CONFIG_HOME=/usr/local/etc
ENV XDG_DATA_HOME=/usr/local/share
ENV XDG_CACHE_HOME=/usr/local/cache
ENV VIMINIT 'let $MYVIMRC="$XDG_CONFIG_HOME/vim/vimrc" | source $MYVIMRC'

RUN apk add -q --no-cache \
  curl docker openssh-client \
  python3 python3-dev \
  mdocml-apropos libc-dev gcc \
  bash fish vim git \
  util-linux bc \
  groff jq gettext coreutils nodejs \
  tmux

RUN python3 -m ensurepip \
  && rm -r /usr/lib/python*/ensurepip \
  && pip3 install --upgrade pip setuptools \
  && rm -rf $XDG_CACHE_HOME

# gotta keep em seperated
RUN pip3 install urwid \
  && pip3 install awscli logentries-lecli sen ctop \
  && rm -rf $XDG_CACHE_HOME

RUN curl --silent -L http://get.oh-my.fish > /tmp/install \
  && fish /tmp/install --noninteractive --path=/usr/local/share/omf --config=/usr/local/etc/omf \
  && rm /tmp/install \
  && rm -rf $XDG_CACHE_HOME

RUN curl -o /usr/local/bin/docker-swarm-diff -fsSL https://github.com/octoblu/docker-swarm-diff/releases/download/v1.0.3/docker-swarm-diff-linux-amd64 \
  && chmod +x /usr/local/bin/docker-swarm-diff \
  && ln -s /usr/local/bin/docker-swarm-diff /usr/local/bin/dsd

RUN mkdir -p /tmp/remarshal \
  && curl --silent -L https://github.com/dbohdan/remarshal/archive/e05b424abacfcf23655c20d891acb51450eba083.tar.gz \
  | tar xzv --strip 1 -C /tmp/remarshal \
  && cd /tmp/remarshal \
  && python3 setup.py install \
  && cd - \
  && rm -rf /tmp/remarshal

# install omf plugins
COPY omf /usr/local/etc/omf
RUN fish -c "omf install"

COPY vim /usr/local/etc/vim
RUN mkdir -p /usr/local/cache/sen
RUN chmod -R 777 /usr/local
