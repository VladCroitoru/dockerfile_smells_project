FROM node:latest
RUN apt-get update -qq && apt-get install -y -qq ocaml libelf-dev && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN curl -o- -L https://yarnpkg.com/install.sh | bash
