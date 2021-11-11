FROM node:16-alpine

ARG PUBLIC_URL_MTL
ARG PUBLIC_URL_THL

ENV PUBLIC_URL_MTL=$PUBLIC_URL_MTL
ENV NODE_ENV=production

WORKDIR /usr/src/mielentila

COPY . .

RUN cd ./frontend && \
    npm ci --production && \
    PUBLIC_URL=$PUBLIC_URL_MTL npm run build 

RUN cd ./thl-frontend && \
    npm ci --production && \
    PUBLIC_URL=$PUBLIC_URL_THL npm run build

RUN cd ./backend && \
    cp -r ../frontend/build builds/mielentilatutkimus && \
    cp -r ../thl-frontend/build builds/thl && \
    rm -rf ../frontend && \
    rm -rf ../thl-frontend && \
    npm ci --production 

EXPOSE 3001

WORKDIR /usr/src/mielentila/backend

CMD PUBLIC_URL=$PUBLIC_URL_MTL npm run prod
