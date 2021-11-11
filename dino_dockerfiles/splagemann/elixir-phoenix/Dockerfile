FROM elixir

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get -y update && apt-get install -y nodejs inotify-tools

VOLUME /usr/src/myapp
WORKDIR /usr/src/myapp

RUN mix local.hex --force
RUN mix archive.install https://github.com/phoenixframework/archives/raw/master/phx_new.ez --force
RUN mix local.rebar --force

EXPOSE 4000

CMD ["mix", "phx.server"]
