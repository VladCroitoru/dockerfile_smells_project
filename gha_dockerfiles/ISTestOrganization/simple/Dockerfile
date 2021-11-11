FROM node:16-alpine AS setup

WORKDIR /workdir

COPY pages pages
COPY public public
COPY \
    next-env.d.ts \
    next.config.js \
    package.json \
    server.js \
    tsconfig.json \
    yarn.lock \
    ./

RUN yarn install

RUN yarn build

CMD ["yarnn", "start"]