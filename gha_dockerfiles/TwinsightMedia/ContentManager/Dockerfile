FROM node:16-buster as BUILDER
COPY ./src /usr/src/frontend/src
COPY ./package.json /usr/src/frontend
COPY ./tsconfig.json /usr/src/frontend
COPY ./webpack.config.js /usr/src/frontend

WORKDIR /usr/src/frontend

RUN npm i
RUN npx webpack


FROM nginx:1.21.1-alpine
COPY ./pages /usr/share/nginx/html/pages/
COPY ./img /usr/share/nginx/html/img
COPY --from=BUILDER /usr/src/frontend/dist/main.js /usr/share/nginx/html/dist/main.js
COPY ./config /usr/share/nginx/html/config
