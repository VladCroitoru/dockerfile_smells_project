# build stage
FROM node:12 AS build-stage
RUN mkdir /app
WORKDIR /app
COPY package*.json /app/
RUN npm ci --only=production

# production stage
FROM node:12-alpine
RUN apk --no-cache add dumb-init
ENV NODE_ENV production
RUN mkdir /app
WORKDIR /app
USER node
COPY --chown=node:node --from=build-stage /app/node_modules /app/node_modules
COPY --chown=node:node . /app
EXPOSE 3000
CMD ["dumb-init", "node", "app.js"]
