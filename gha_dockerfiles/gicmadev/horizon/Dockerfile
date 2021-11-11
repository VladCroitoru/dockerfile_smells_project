FROM elixir:1.9 as runner

EXPOSE 4000
ENV MIX_HOME=/.mix

RUN apt-get update \
    && apt-get -y --no-install-recommends install libtag1-dev \
    && apt-get purge -y --auto-remove

WORKDIR /app

CMD ["mix", "phx.server"]

FROM node as node-builder

WORKDIR /app

COPY package*.json /app/
RUN npm install

COPY ./assets /app/assets
COPY .babelrc /app/
COPY ./webpack.config.js /app

RUN npm run deploy

FROM runner as horizon

ADD mix.exs .
ADD mix.lock .

ENV MIX_ENV=prod
ENV LANG=C.UTF-8

RUN mix local.rebar --force

RUN mix local.hex --force

RUN mix deps.get --only prod

RUN mix deps.compile

COPY --from=node-builder /app/priv/static/js /app/priv/static/js

WORKDIR /app

ADD . .

RUN useradd -u 1004 app

RUN chown -R app: /app

USER app

EXPOSE 4000

ENTRYPOINT ["mix"]
CMD ["phx.server"]
