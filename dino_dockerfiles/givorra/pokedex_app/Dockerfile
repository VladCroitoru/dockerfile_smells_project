# base image elixer to start with
FROM elixir:latest

# install hex package manager
RUN mix local.hex --force

# install the latest phoenix
RUN mix archive.install https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez --force

RUN mix local.rebar --force

# install node
RUN curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt-get install nodejs

# install inotify-tools
RUN apt-get install -y inotify-tools

# create app folder
RUN mkdir /app
COPY . /app
WORKDIR /app
