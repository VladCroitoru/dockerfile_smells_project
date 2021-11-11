FROM starefossen/ruby-node:2-8


RUN mkdir -p /local

COPY Gemfile /local
COPY Gemfile.lock /local

WORKDIR /local

RUN bundle install --system

RUN npm install -g widdershins@3.6.6 node-fetch@2.2.0 json-stable-stringify@1.0.1 swagger-cli@4.0.3
