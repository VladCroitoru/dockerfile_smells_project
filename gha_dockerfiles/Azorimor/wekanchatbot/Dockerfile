# Stage 1 Builder
FROM node:14-alpine as builder
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
WORKDIR /home/node/app
COPY package*.json ./

# RUN npm config set unsafe-perm true
# RUN npm install -g typescript
# RUN npm install -g ts-node

USER node
RUN npm install
COPY --chown=node:node . .
RUN npm run build

# Stage 2 actual bot
FROM node:14-alpine as bot
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
WORKDIR /home/node/app
COPY package*.json ./
USER node

ENV NODE_ENV production

RUN npm install --production
COPY --from=builder /home/node/app/dist ./dist

# COPY --chown=node:node .env .

EXPOSE 3000
CMD [ "node", "dist/index.js" ]