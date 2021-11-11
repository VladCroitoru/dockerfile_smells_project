FROM roosoft/elixir-build:1.12.2 as builder

ENV MIX_ENV prod
ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ENV DATABASE_URL ecto://USER:PASS@HOST/DATABASE
ENV SECRET_KEY_BASE im6Sc4GdO7LRX9FflsM5sOxP/QYBgcvVq4ixCkEZ/UB1islMllpEk9VrRaeNi5u2

COPY . steer

RUN cd steer && \
    mix local.hex --force && \
    mix archive.install hex phx_new 1.5.3 --force && \
    mix local.rebar --force && \
    mix do deps.get, deps.compile 

RUN cd steer/assets && \
    npm i && \
    npm run deploy

RUN cd steer && \
    mix compile && \
    mix phx.digest && \
    MIX_ENV=prod mix release


FROM alpine:latest as app

ENV LANG=C.UTF-8

RUN apk update && apk add openssl ncurses-libs libstdc++

RUN adduser -h /home/app -D app
WORKDIR /home/app
COPY --from=builder /app/steer/_build/prod/rel/standard .
RUN chown -R app: .
USER app

CMD ["./bin/standard", "start"]
EXPOSE 4000
