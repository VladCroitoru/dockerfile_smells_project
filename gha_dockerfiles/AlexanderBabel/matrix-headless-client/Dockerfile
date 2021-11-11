#
# Builder stage.
# This state compile our TypeScript to get the JavaScript code
#
FROM node:16.13.0-bullseye AS builder

WORKDIR /usr/src/app

COPY . .

RUN curl -sfL https://gobinaries.com/tj/node-prune | bash -s -- -b /usr/local/bin

RUN yarn install --frozen-lockfile --silent --network-timeout 100000

RUN yarn build

RUN yarn install --production --frozen-lockfile --silent && /usr/local/bin/node-prune && rm -rf src/

#
# Production stage.
# This state compile get back the JavaScript code from builder stage
# It will also install the production package only
#
FROM node:16.13.0-alpine3.14

WORKDIR /app

ENV NODE_ENV=production
ENV NODE_PATH=/app/dist/

## We just need the build to execute the command
COPY --from=builder /usr/src/app/. .

## uncomment following line, if you want to mount the templates folder
#COPY ./templates /app/templates

## uncomment following line, if you want to mount the public folder
#COPY ./public /app/public

ENTRYPOINT [ "node" ]
CMD [ "dist/main.js" ]

EXPOSE 5000
