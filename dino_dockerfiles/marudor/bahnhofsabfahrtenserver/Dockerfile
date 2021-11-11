FROM node:10-alpine as build
WORKDIR /app
COPY package.json /app/
COPY yarn.lock /app/
COPY .flowconfig /app/
COPY .babelrc.js /app/
RUN yarn
COPY src/ /app/src/
RUN yarn build

FROM node:10-alpine
RUN mkdir -p /app
WORKDIR /app
COPY --from=build /app/lib /app/lib/
COPY package.json /app
COPY yarn.lock /app/
ENV NODE_ENV=production
RUN yarn --prod
CMD [ "yarn", "start" ]
