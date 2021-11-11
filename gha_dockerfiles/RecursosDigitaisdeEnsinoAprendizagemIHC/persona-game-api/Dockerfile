FROM node:14

# Create app directory
WORKDIR /usr/src/app/persona-game-api

# Installing dependencies
COPY persona-game-api/package*.json ./
COPY persona-game-api/yarn.lock ./
RUN yarn install

EXPOSE 8000

# Running the app
CMD ["yarn", "dev"]
