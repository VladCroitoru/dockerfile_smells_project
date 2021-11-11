FROM elixir:1.3.2-slim

MAINTAINER Lucas Saboya <lucas.saboya@gmail.com>

ENV MIX_ENV prod

RUN apt-get update && \
apt-get -y install --no-install-recommends wget git openssl && \
rm -rf \
/var/lib/apt/lists/* \
/tmp/* \
/var/tmp/*

RUN wget --no-check-certificate https://github.com/luizbafilho/hydra/releases/download/v0.2/hydra -O /usr/bin/hydra

RUN chmod +x /usr/bin/hydra

RUN epmd -daemon

CMD "/usr/bin/hydra"
