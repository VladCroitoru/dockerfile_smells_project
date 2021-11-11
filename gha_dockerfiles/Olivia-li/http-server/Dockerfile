FROM node:14-alpine
ENV NODE_ENV=production
WORKDIR /usr/src/app
COPY ["package.json", "package-lock.json", "yarn.lock", "./"]
RUN yarn --production --silent && mv node_modules ../
COPY . .
EXPOSE 8080
RUN chown -R node /usr/src/app
USER node
CMD ["node", "Services/HttpServerService.js"]
