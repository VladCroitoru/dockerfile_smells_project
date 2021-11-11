FROM node:carbon-alpine
ENV NODE_ENV production
WORKDIR /usr/src/app
COPY ["package.json", "yarn.lock", "./"]
RUN yarn install --production --silent
COPY . .
EXPOSE 3000
CMD yarn start