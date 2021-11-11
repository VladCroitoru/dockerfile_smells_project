FROM zorbash/kitto

ENV MIX_ENV prod

RUN mkdir /dashboard
WORKDIR /dashboard

COPY ./mix.exs ./
COPY ./mix.lock ./
COPY ./package.json ./
RUN mix deps.get && npm install --silent

COPY . /dashboard

# RUN mix compile
# CMD ["mix", "kitto.server"]
RUN mix release --env=prod

CMD ["/dashboard/_build/prod/rel/cd_dash/bin/cd_dash", "foreground"]
