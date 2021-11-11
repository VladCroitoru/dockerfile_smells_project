FROM node:6.10-slim

LABEL maintainer "gene@technicalissues.us"

ENV APP_ROOT /var/www
RUN mkdir -p $APP_ROOT
WORKDIR $APP_ROOT

COPY package.json $APP_ROOT/package.json
RUN npm install --production

# Temp patch pending the merging of https://github.com/chamerling/dockerhub2slack/pull/2
# Post-merge the package.json file will need updating.
RUN curl -o node_modules/dockerhub2slack/dist/server/index.js https://raw.githubusercontent.com/genebean/dockerhub2slack/genebean/server/index.js

EXPOSE 3000
CMD [ "npm", "start" ]

