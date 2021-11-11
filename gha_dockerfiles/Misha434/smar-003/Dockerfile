FROM ruby:2.6.3

RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -\
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update -qq \
    && apt-get install -y --no-install-recommends \
       imagemagick \
       nodejs \
       mariadb-client \
       yarn

WORKDIR /smar-003

COPY Gemfile* /smar-003
RUN bundle install -j4 \
    && yarn install --check-files

COPY . /smar-003

COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000

CMD ["foreman", "start"]