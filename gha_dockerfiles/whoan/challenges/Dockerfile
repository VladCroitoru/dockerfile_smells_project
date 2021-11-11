FROM alpine:3

RUN apk add --no-cache \
  binutils-gold \
  g++ \
  libstdc++ \
  linux-headers \
  cmake \
  make \
  curl \
  jq \
  grep \
  file \
  bash

WORKDIR /app

VOLUME ~/.cache

ADD https://raw.githubusercontent.com/whoan/snip/master/snip.sh ./snip.sh
RUN \
  mkdir -p ~/.config/snip/ && \
  echo 'source /app/snip.sh' >> ~/.bashrc && \
  echo -e 'snip() {\n __snip "$@"\n}' >> ~/.bashrc && \
  echo 'base_url=https://raw.githubusercontent.com/whoan/snippets/master/' > ~/.config/snip/settings.ini

ADD https://raw.githubusercontent.com/whoan/tst/master/tst.sh ./tst.sh
RUN \
  mkdir -p ~/.config/tst/ && \
  echo 'source /app/tst.sh' >> ~/.bashrc && \
  echo 'base_url=https://api.github.com/repos/whoan/datasets/contents' > ~/.config/tst/settings.ini

COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
