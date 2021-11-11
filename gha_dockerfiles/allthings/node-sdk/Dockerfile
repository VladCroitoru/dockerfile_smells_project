FROM allthings/node

COPY --chown=node:node . /srv/www/node-sdk
WORKDIR /srv/www/node-sdk

USER node
RUN yarn install --ignore-scripts --production=false --frozen-lockfile --silent --non-interactive \
  && yarn cache clean \
  && yarn build

ENV PATH "$PATH:/srv/www/node-sdk/node_modules/.bin"

ENTRYPOINT ["tini", "-g", "--"]
