FROM ubuntu:latest AS base

RUN \
  apt update \
  && apt install -y --no-install-recommends \
    build-essential \
    libsqlite3-dev \
    libstfl-dev \
    libcurl4-openssl-dev \
    pkg-config \
    libxml2-dev \
    libjson-c-dev \
    libncursesw5-dev \
    libssl-dev \
    gettext \
    git \
    elinks \
    curl \
    jq \
    asciidoc-base

RUN \
  apt install ca-certificates -y && \
  git clone https://github.com/newsboat/newsboat.git /code

# includes Makefile hack to avoid installing docs
RUN \
  cd /code && \
  sed '/A2X=.*/ { s,A2X=.*,A2X=printf --, }' -i Makefile && \
  sed '/^doc: .*/ { s,doc: .*,doc:, }' -i Makefile && \
  make && \
  make install

# ---

FROM ubuntu:latest

RUN \
  groupadd rss && \
  useradd rss -g rss -d /home/rss && \
  mkdir -p /home/rss/.newsbeuter && \
  chown -R rss:rss /home/rss

RUN apt update \
    && apt install -y --no-install-recommends \
      curl \
      elinks \
      jq

ENV HOME /home/rss
USER rss
WORKDIR ${HOME}


CMD ["/usr/local/bin/newsboat"]

COPY --from=base /usr/local/bin/newsboat /usr/local/bin/newsboat

