# Note that this Docker configuration is exclusively for starting up the server on a local machine so that experiments can be run by researchers even without any internet connection. The production web app is NOT deployed via Docker for now.
FROM elixir:1.6

MAINTAINER JI Xiang <hi@xiangji.me>

RUN mix local.hex --force \
 && mix archive.install --force https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez \
 && apt-get update \
 && curl -sL https://deb.nodesource.com/setup_6.x | bash \
 && apt-get install -y apt-utils \
 && apt-get install -y nodejs \
 && apt-get install -y build-essential \
 && apt-get install -y inotify-tools \
 && mix local.rebar --force

RUN mkdir /app
# Copy all the files in the current git repo into the target /app folder
COPY . /app
# Similar to cd
WORKDIR /app

EXPOSE 4000

# This thing apparently isn't working. No idea why.
#RUN mix deps.get \
#&& mix deps.compile \
#&& npm install \
#&& node node_modules/brunch/bin/brunch build

CMD ["mix", "phx.server"]
