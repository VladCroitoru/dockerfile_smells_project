FROM elixir:1.9.4

RUN apt-get update \
    && apt-get install -y software-properties-common curl apt-transport-https git \
    && add-apt-repository -y "deb https://cli-assets.heroku.com/branches/stable/apt ./"

RUN curl -L https://cli-assets.heroku.com/apt/release.key | apt-key add -
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -

RUN apt-get update -qy && apt-get install -y \
    nodejs \
    heroku \
    postgresql-client \
    rubygems \
    poppler-utils

RUN gem install dpl

RUN npm install -g \
    elm@0.19.0 \
    elm-test@0.19.0

CMD ["iex"]
