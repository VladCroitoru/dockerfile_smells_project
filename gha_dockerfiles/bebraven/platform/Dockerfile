FROM ruby:3.0.2

# Changes the default shell from dash to bash. Our docker_compose_run.sh
# script has a syntax error when run in dash.
RUN export DEBIAN_FRONTEND=noninteractive; \
    export DEBCONF_NONINTERACTIVE_SEEN=true; \
    dpkg-reconfigure -f noninteractive dash

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee etc/apt/sources.list.d/yarn.list \
    && curl -fsSL https://deb.nodesource.com/setup_12.x | bash - \
    && apt-get update -qq \
    && apt-get install -y vim \
    && apt-get install -y nodejs yarn tzdata libnotify-dev \
    && rm -rf /var/lib/apt/lists/*

# Allow local builds to change it. Defaults to development.
ARG RAILS_ENV=development
ENV RAILS_ENV ${RAILS_ENV}
ENV NODE_ENV=${RAILS_ENV}

WORKDIR /app

COPY Gemfile Gemfile.lock /app/

RUN bundle config set --local path 'vendor/bundle' && \
    bundle install --jobs 4 && cp Gemfile.lock /tmp

COPY . /app/

CMD ["/bin/bash"]
