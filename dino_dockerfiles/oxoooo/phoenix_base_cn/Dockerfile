FROM elixir:1.4.2
MAINTAINER mj <tywf91@gmail.com>

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install -y nodejs
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install yarn

RUN mkdir -p /opt/node_tmp
WORKDIR /opt/node_tmp

RUN yarn add node-sass@4.5.0
