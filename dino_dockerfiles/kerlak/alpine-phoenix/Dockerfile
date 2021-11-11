FROM alpine
MAINTAINER Juan Carlos Pazos Mandiá <jucapaman@gmail.com>
RUN apk update
RUN apk add erlang\
            erlang-crypto\
            erlang-syntax-tools\
            erlang-parsetools\
            elixir\
            nodejs\
            git
RUN yes | mix archive.install https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez
RUN yes | mix local.hex
RUN yes | mix local.rebar
