FROM elixir

RUN apt-get update && apt-get install -y \
    curl &&\
    curl -sL https://deb.nodesource.com/setup_6.x | bash /dev/stdin &&\
    apt-get install -y nodejs git-all &&\
    apt-get clean -y && \
    rm -rf /var/cache/apt/*

RUN npm install -g brunch && \
    yes | mix local.hex && \
    yes | mix local.rebar && \
    yes | mix archive.install https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez

WORKDIR /srv
VOLUME /srv
