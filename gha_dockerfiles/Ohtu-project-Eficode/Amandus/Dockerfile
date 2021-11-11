FROM node:14-alpine AS front-build-stage

COPY ./frontend ./frontend
WORKDIR /frontend
RUN yarn && yarn build

FROM node:14-alpine

RUN mkdir -p /usr/src/app/
COPY ./backend /usr/src/app/backend
WORKDIR /usr/src/app/backend
RUN apk add git && yarn && yarn build 
COPY --from=front-build-stage /frontend/build/ /usr/src/app/backend/build/frontBuild

EXPOSE 3001

CMD ["yarn","start"]