FROM node:14-alpine
ENV PORT=10404
WORKDIR /usr/src/app
COPY ["package.json", "package-lock.json*", "yarn.lock", "npm-shrinkwrap.json*", "./"]
RUN yarn install && mv node_modules ../
COPY . .
EXPOSE 10404
# RUN chown -R node /usr/src/app
# USER node
CMD ["yarn", "start"]
