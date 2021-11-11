# File: travl_life/Dockerfile
FROM elixir:1.12-slim as build

# install build dependencies
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    git \
    build-essential \
    python3

# Be sure we install node 12
RUN apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt -y install nodejs

RUN mkdir /app
WORKDIR /app

# install Hex + Rebar
RUN mix do local.hex --force, local.rebar --force

# set build ENV
ENV MIX_ENV=prod

# install mix dependencies
COPY mix.exs mix.lock ./
COPY config config
RUN mix deps.get --only $MIX_ENV
RUN mix deps.compile

COPY lib lib
COPY assets assets
COPY priv priv

# build assets
RUN npm install --prefix ./assets
RUN mix compile surface
RUN mix assets.deploy
RUN mix phx.digest

# build project, compile surface so we have JS hooks
RUN mix compile

# build release
# at this point we should copy the rel directory but
# we are not using it so we can omit it
# COPY rel rel
RUN mix release

# prepare release image
FROM debian:buster-slim AS app

# install runtime dependencies
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    bash \
    openssl \
    ca-certificates \
    postgresql-client \
    locales

ENV LANG=en_US.UTF-8
RUN echo $LANG UTF-8 > /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=$LANG

EXPOSE 4000
ENV MIX_ENV=prod

# prepare app directory
RUN mkdir /app
RUN mkdir /app/certs
WORKDIR /app

# preapre data directory
# RUN mkdir -p /app/data/mnesia

# copy release to app container
COPY --from=build /app/_build/prod/rel/commentator .
COPY priv/certs ./certs
COPY entrypoint.sh .
RUN chown -R nobody: /app
USER nobody

VOLUME /app/data

ENV HOME=/app
CMD ["bash", "/app/entrypoint.sh"]
