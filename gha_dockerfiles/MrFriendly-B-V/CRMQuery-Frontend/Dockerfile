FROM node:16-buster as builder
COPY ./ /usr/local/src/
WORKDIR /usr/local/src/

RUN npm i
RUN npx webpack

FROM nginx:1.21.1-alpine
COPY --from=builder /usr/local/src/dist/* /usr/share/nginx/html/dist/
COPY ./img/* /usr/share/nginx/img/
COPY ./*.html /usr/share/nginx/html/
COPY ./config.json /usr/share/nginx/html/config.json