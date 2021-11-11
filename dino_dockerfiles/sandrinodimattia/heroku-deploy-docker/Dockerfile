FROM ruby:2.3

RUN apt-get update \
    && apt-get install -y software-properties-common curl apt-transport-https \
    && add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./" \
    && curl -L https://cli-assets.heroku.com/apt/release.key | apt-key add - \
    && apt-get update \
    && apt-get install -y heroku \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && apt-get autoremove -y

RUN gem install dpl -v 1.8.38
