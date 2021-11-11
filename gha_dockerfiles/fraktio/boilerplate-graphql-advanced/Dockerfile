FROM node:14-slim as build
WORKDIR /app

# Copy application dependency manifests to the container image.
COPY package.json ./
COPY package-lock.json ./
RUN npm ci

# Copy local code to the container image and build
COPY . ./
RUN npm run build


FROM node:14-slim as release
WORKDIR /home/node
COPY --chown=node:node --from=build /app/dist ./
RUN rm -rf /app
USER node

ENV NODE_ENV=production
RUN npm ci

ENV API_PORT=8080
EXPOSE 8080
CMD [ "node", "./main.js" ]
