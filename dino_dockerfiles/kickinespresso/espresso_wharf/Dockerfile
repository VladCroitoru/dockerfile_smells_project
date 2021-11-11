FROM ubuntu:16.04

LABEL maintainer="KickinEspresso"
LABEL email="contact@kickinespreso.com"
LABEL website="kickinespresso.com"
LABEL project_link="https://github.com/kickinespresso/espresso_wharf"
LABEL version="0.1.0"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && apt-get install -y wget curl locales build-essential libpq-dev git inotify-tools apt-utils
RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && dpkg -i erlang-solutions_1.0_all.deb
RUN apt-get update -qq && apt-get install esl-erlang -y
RUN apt-get install elixir -y

#Set Locale
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

#Build hex
RUN mix local.hex --force && mix local.rebar --force

# Get Latest Version of NodeJS (9.x)
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -
RUN apt-get install -y nodejs

# Other stuff
# RUN mkdir /expresso_wharf_phoenix
# WORKDIR /expresso_wharf_phoenix
# COPY mix.lock /expresso_wharf_phoenix/mix.lock
# COPY mix.exs /expresso_wharf_phoenix/mix.exs
# RUN mix deps.get
# #RUN npm install
# COPY . /expresso_wharf_phoenix
# RUN cd assets && npm install && node node_modules/brunch/bin/brunch build

#EXPOSE 4000
