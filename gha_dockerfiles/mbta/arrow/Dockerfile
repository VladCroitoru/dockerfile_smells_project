FROM hexpm/elixir:1.11.4-erlang-23.3-debian-buster-20210208 as builder

ENV LANG=C.UTF-8 \
  MIX_ENV=prod

RUN apt-get update --allow-releaseinfo-change && \
  apt-get install -y --no-install-recommends ca-certificates curl git

# Instructions from:
# https://github.com/nodesource/distributions/blob/master/README.md
RUN  curl -sL https://deb.nodesource.com/setup_14.x | bash - \
  && apt-get install -y nodejs \
  && npm install -g npm@latest

WORKDIR /root
ADD . .

RUN mix local.hex --force && \
  mix local.rebar --force && \
  mix do deps.get --only prod, compile --force && \
  mix esbuild.install && \
  npm --prefix assets ci && \
  mix assets.deploy && \
  mix release

FROM debian:buster

RUN apt-get update --allow-releaseinfo-change && \
  apt-get install -y --no-install-recommends libssl1.1 libsctp1 curl && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /root
EXPOSE 4000
ENV MIX_ENV=prod TERM=xterm LANG="C.UTF-8" PORT=4000

COPY --from=builder /root/_build/prod/rel/arrow .

CMD ["bin/arrow", "start"]
