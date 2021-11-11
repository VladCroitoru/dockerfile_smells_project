FROM ruby:3.0.2

RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
RUN apt-get update &&     apt-get install postgresql-client nano nodejs -y &&     npm install --global yarn

WORKDIR /var/app

COPY Gemfile /var/app/Gemfile
COPY Gemfile.lock /var/app/Gemfile.lock
COPY package.json /var/app/package.json
COPY yarn.lock /var/app/yarn.lock
RUN bundle install
RUN yarn install

COPY . /var/app

COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000

CMD ["rails", "server", "-b", "0.0.0.0"]
