FROM node:16.1

WORKDIR /var/app
RUN mkdir -p /var/app
ADD package.json yarn.lock /var/app/
RUN yarn install

COPY . /var/app

RUN yarn build

ENV PORT 8080
ENV NODE_ENV production

EXPOSE 8080

CMD [ "yarn", "run", "production" ]

# uncomment the lines below to run it in development mode
# ENV NODE_ENV development
# CMD [ "yarn", "run", "start" ]
