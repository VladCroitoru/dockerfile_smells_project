### Build stage
FROM node:14.16-alpine as builder

ENV HOME=/home/app
ENV APP_PATH=$HOME/editorial-frontend

# Copy necessary files for installing dependencies
COPY yarn.lock package.json $APP_PATH/

# Run yarn before src copy to enable better layer caching
WORKDIR $APP_PATH
RUN yarn

# Copy necessary source files for server and client build
COPY .babelrc tsconfig.json razzle.config.js postcss.config.js $APP_PATH/

COPY src $APP_PATH/src
COPY custom-typings $APP_PATH/custom-typings
COPY public $APP_PATH/public

# Build client code
RUN yarn run build

### Run stage
FROM node:14.16-alpine

RUN apk add py2-pip jq && pip install awscli
COPY run-editorial-frontend.sh /


RUN npm install pm2 -g
WORKDIR /home/app/editorial-frontend
COPY --from=builder /home/app/editorial-frontend/build build

ENV NODE_ENV=production

CMD ["/run-editorial-frontend.sh", "pm2-runtime -i max build/server.js '|' bunyan"]
