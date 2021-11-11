FROM elixir:1.9.4

RUN apt-get update && \
    apt-get install -y postgresql-client curl inotify-tools

RUN mkdir /app
WORKDIR /app

# Install hex package manager
RUN mix local.rebar --force
RUN mix local.hex --force
COPY mix.exs .
RUN mix deps.get && mix deps.compile

# Installing node
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
WORKDIR /app/assets
RUN npm install
RUN npm rebuild node_sass

# Compile the project
WORKDIR /app
COPY . /app
RUN mix compile && chmod +x entrypoint.sh
ENV PGHOST=db
ENV PGPORT=5432

CMD ["mix", "phx.server"]
