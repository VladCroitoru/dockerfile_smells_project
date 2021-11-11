FROM trenpixster/elixir:latest
MAINTAINER Adam Smith <adam@akuseru.io>

RUN apt-get update && apt-get install -qy nodejs npm postgresql-client --no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /
#RUN npm update
#RUN mix deps.get

ENV PORT 8080
ENV MIX_ENV dev

#RUN mix deps.compile

EXPOSE 8080

#ENTRYPOINT mix test
