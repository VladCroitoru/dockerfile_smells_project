FROM mhart/alpine-node:12

ENV NODE_ENV=production
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
ENV DISABLE_SERVERLESS=true
ENV IS_DOCKER=true

WORKDIR /usr/src/app/client

COPY package.json package.json
COPY .next .next
COPY next.config.js next.config.js
COPY env.js env.js

# will throw "error Couldn't find the binary git" without git (since we have a tar/github repo in deps)
# https://stackoverflow.com/questions/50837605/git-install-fails-in-dockerfile
# https://github.com/nodejs/docker-node/issues/586
# https://github.com/gliderlabs/docker-alpine/blob/master/docs/usage.md#virtual-packages
RUN apk add git

# @todo - pure-lockfile --frozen
RUN yarn install \
  --production \
  --network-timeout 1000000 \
  --ignore-optional --skip-integrity-check \
  --ignore-scripts \
  --ignore-engines && \
  yarn cache clean

RUN ls -la . && cd .next && ls -la . && echo "hash2"

RUN apk del git

EXPOSE 3000
EXPOSE 80

CMD ["npx", "next", "start"]
# CMD ["yarn", "start"]
# CMD ["pm2-runtime", "dist/ecosystem.docker.config.js"]

