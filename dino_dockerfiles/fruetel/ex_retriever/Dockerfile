FROM elixir:1.6.2-slim

RUN groupadd -r app -g 1000
RUN useradd -u 1000 -r -g app -m -s /sbin/nologin app

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y git curl wget build-essential

RUN mkdir /code
RUN chown app:app /code
USER app

RUN mix local.hex --force
RUN mix local.rebar --force

WORKDIR /code

COPY --chown=app:app ./mix.exs /code/
COPY --chown=app:app ./mix.lock /code/

ENV MIX_ENV prod
RUN mix deps.get
RUN mix deps.compile

COPY --chown=app:app . /code

RUN mix compile

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["run"]
