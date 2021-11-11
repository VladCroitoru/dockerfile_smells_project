# stage 1 building the code

FROM node:14-alpine as builder

ENV NODE_ENV build

USER node
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN npm ci \
    && npm run build \
    && npm prune --production

FROM node:14-alpine 
USER node
WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/dist/ /usr/src/app/dist/
COPY --from=builder /usr/src/app/node_modules/ /usr/src/app/node_modules/
COPY --from=builder /usr/src/app/package*.json /usr/src/app/
COPY --from=builder /usr/src/app/.env /usr/src/app/

RUN ls -a

CMD [ "node", "dist/main.js" ]

# FROM node:14-alpine

# ENV NODE_ENV production

# USER node
# WORKDIR /home/node

# COPY --from=builder /home/node/package*.json /home/node/
# COPY --from=builder /home/node/node_modules/ /home/node/node_modules/
# COPY --from=builder /home/node/dist/ /home/node/dist/

# CMD ["node", "dist/server.js"]

