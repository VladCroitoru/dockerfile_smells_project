FROM node:12-alpine
WORKDIR /usr/src/app
LABEL Description="A2R Watcher"
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
RUN npm install --production --silent
COPY . ./src
RUN rm -rf ./src/server
RUN cd ./src;npm install --silent;npm run build;mv ./bin/* ../;cd ..;rm -rf ./src
VOLUME ["/usr/src/app/server"]
ENV NODE_ENV production
CMD npm start