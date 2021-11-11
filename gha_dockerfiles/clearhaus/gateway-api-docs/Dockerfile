FROM node:stretch

RUN apt-get update \
    && apt-get install -y ruby2.3 bundler \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD ./Gemfile /tmp/Gemfile
ADD ./Gemfile.lock /tmp/Gemfile.lock
ADD ./bower.json /tmp/bower.json
WORKDIR /tmp

RUN bundle install
RUN npm install -g bower
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN echo Y | bower install --allow-root

ADD ./ /web
WORKDIR /web

EXPOSE 4567
CMD bundle exec middleman
