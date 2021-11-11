FROM node:12.22.3-alpine AS dependencies
WORKDIR /usr/src/app

ADD package.json .
ADD yarn.lock .
RUN yarn install


FROM dependencies AS build

ADD . .

RUN yarn build


FROM build AS test

RUN yarn test

FROM node:12.22.3-alpine AS assemble
WORKDIR /usr/src/app

COPY package.json .
COPY yarn.lock .
RUN yarn install --production

COPY --from=build /usr/src/app/dist dist


ENTRYPOINT ["yarn", "start"]
