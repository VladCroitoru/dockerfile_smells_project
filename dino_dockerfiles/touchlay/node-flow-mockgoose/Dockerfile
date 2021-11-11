FROM node:latest
RUN apt-get update -qq && apt-get install -y -qq ocaml libelf-dev && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN npm install mockgoose mongoose && node -e "var mongoose = require('mongoose'); var Mockgoose = require('mockgoose').Mockgoose; var mockgoose = new Mockgoose(mongoose); mockgoose.prepareStorage().then(() => process.exit(0))"
