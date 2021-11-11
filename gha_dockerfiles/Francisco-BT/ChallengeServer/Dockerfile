FROM node:14.17.6 AS client_build
RUN yarn install
WORKDIR /usr/src/app
COPY client/ ./client/
RUN cd client && yarn && yarn build

FROM node:14.17.6 AS server_build
ENV NODE_ENV=production
WORKDIR /usr/src/server
COPY --from=client_build /usr/src/app/client/build ./client/build
COPY server/package.json ./server/
COPY server/yarn.lock ./server
RUN cd server && yarn --production
COPY server/ ./server/


EXPOSE 80
CMD ["node", "./server/index.js"]

