# pull official base image. As builder for production
FROM node:14-buster-slim as build

WORKDIR /app

RUN yarn global add gatsby-cli && gatsby telemetry --disable

ADD package.json yarn.lock ./

RUN yarn --production --non-interactive

ADD . ./

RUN gatsby build

EXPOSE 9000

# serve using Node serve package from build directory
CMD ["gatsby", "serve", "-H", "0.0.0.0"]