FROM ubuntu

RUN    apt-get update \
    && apt-get install -y software-properties-common curl apt-transport-https git \
    && add-apt-repository -y "deb https://cli-assets.heroku.com/branches/stable/apt ./" \
    && curl -L https://cli-assets.heroku.com/apt/release.key | apt-key add - \
    && apt-get update \
    && apt-get install -y heroku postgresql-client \
    && apt-get clean \
    && heroku plugins:install heroku-cli-deploy
