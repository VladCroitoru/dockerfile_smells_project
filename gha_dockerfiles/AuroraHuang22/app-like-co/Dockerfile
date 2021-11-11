FROM node:14
WORKDIR /app
COPY ./package.json ./
COPY ./yarn.lock ./
RUN yarn install
ARG IS_TESTNET
ENV IS_TESTNET ${IS_TESTNET}
ARG GA_TRACKING_ID
ENV GA_TRACKING_ID ${GA_TRACKING_ID}
ENV NODE_ENV production
COPY ./ ./
RUN yarn build
EXPOSE 3000
CMD yarn start
