FROM  node:14-alpine

# Pass env from docker-compose
ARG NODE_ENV

WORKDIR /app
COPY package.json yarn.lock $HOMR/app/
RUN yarn
COPY . .
