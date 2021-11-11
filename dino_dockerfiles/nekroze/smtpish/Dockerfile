FROM elixir:latest as builder

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
RUN apt-get -qq update \
 && apt-get -qq install git build-essential

RUN mix local.hex --force && \
    mix local.rebar --force && \
    mix hex.info

WORKDIR /app
ENV MIX_ENV prod
ADD . .
RUN rm -rf _build deps
RUN mix deps.get
RUN mix release --env=$MIX_ENV


FROM debian:jessie-slim

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
RUN apt-get -qq update \
 && apt-get -qq install libssl1.0.0 libssl-dev

WORKDIR /app
COPY --from=builder /app/_build/prod/rel/smtpish .

CMD ["./bin/smtpish", "foreground"]
