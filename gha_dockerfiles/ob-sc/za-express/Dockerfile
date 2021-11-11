FROM node:16
WORKDIR /usr/src/app
COPY package.json yarn.lock ./
RUN yarn install
# yarn install --production
COPY . .
RUN yarn build
EXPOSE 8000
CMD [ "yarn", "start" ]
