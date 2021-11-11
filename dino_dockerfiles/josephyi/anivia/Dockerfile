FROM josephyi/phoenixframework:1.0.5
RUN apk --update add erlang-tools && rm -rf /var/cache/apk/*
WORKDIR /app
ENV MIX_ENV prod
ENV NODE_ENV production
ENV PORT=4000

COPY . /app
RUN yes | mix local.hex && yes | mix local.rebar && npm install && mix do deps.get && MIX_ENV=prod mix compile && mix phoenix.digest
VOLUME ["/app"]
CMD ["mix", "phoenix.server"]
