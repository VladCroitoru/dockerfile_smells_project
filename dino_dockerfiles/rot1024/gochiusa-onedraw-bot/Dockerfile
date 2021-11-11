FROM node:6-alpine
MAINTAINER rot1024

RUN npm i -g yarn && mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD package.json yarn.lock /usr/src/app/
RUN yarn install
COPY . /usr/src/app/
VOLUME /usr/src/app/data

# ENV GODB_TWITTER_CONSUMER_KEY
# ENV GODB_TWITTER_CONSUMER_SECRET
# ENV GODB_TWITTER_ACCESS_TOKEN
# ENV GODB_TWITTER_ACCESS_TOKEN_SECRET

CMD ["yarn", "start"]
