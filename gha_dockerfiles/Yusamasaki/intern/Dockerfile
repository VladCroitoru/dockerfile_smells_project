FROM ruby:2.7.3

LABEL name="Artificial intern" version="1.0" description="Artificial intern"

ARG rails_arg="development"
# ARG rails_arg="production"

# 色々インストール
RUN apt-get update && apt-get -y install gosu sudo apt-utils

# nodejsインストール
RUN curl -fsSL https://deb.nodesource.com/setup_current.x | bash - && \
apt-get update && apt-get -y install --no-install-recommends nodejs

# postgresqlインストール
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update && apt-get -y install --no-install-recommends postgresql-12 postgresql-client-12

# yarnインストール
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
apt-get update && apt-get -y install --no-install-recommends yarn

# axiosインストール
RUN yarn add axios

RUN mkdir /myapp
WORKDIR /myapp
COPY ./src /myapp
RUN bundle config --local set path 'vendor/bundle' && bundle install

# entrypoint.shをコピーし、実行権限を与える
COPY entrypoint_${rails_arg}.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT [ "entrypoint.sh" ]
EXPOSE 3000

CMD [ "rails", "server", "-b", "0.0.0.0" ]