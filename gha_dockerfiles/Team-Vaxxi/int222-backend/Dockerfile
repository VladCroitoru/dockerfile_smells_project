FROM node:14.16.1-alpine3.10
WORKDIR /app
COPY package*.json ./
RUN yarn
COPY ./ .
RUN yarn build
CMD ["yarn", "start:prod"]