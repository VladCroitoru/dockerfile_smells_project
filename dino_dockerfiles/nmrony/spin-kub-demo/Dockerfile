FROM node:6-alpine
ENV NODE_ENV production
WORKDIR /usr/src/app
COPY ["package.json", "yarn.lock", "npm-shrinkwrap.json*", "./"]
RUN yarn install
COPY . .
EXPOSE 8000
CMD npm start