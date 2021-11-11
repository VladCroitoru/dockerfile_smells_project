FROM ruby:3.0.1

RUN apt-get update -qq \
   && rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g yarn

WORKDIR /locat
COPY . /locat
RUN gem install bundler
RUN bundle install
RUN yarn install
#RUN yarn build
EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]
