FROM node:12-alpine as build

COPY . /usr/build

WORKDIR /usr/build

RUN npm install && npm run build

FROM node:12-alpine as app

COPY --from=build /usr/build/public /app

WORKDIR /app

ENV NODE_ENV production
ENV HOST 0.0.0.0
ENV PORT 80

WORKDIR /app

RUN npm install -g sirv-cli && npm cache clean --force 

EXPOSE 80

ENTRYPOINT ["sirv", "/app", "--single"]