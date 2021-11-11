FROM node:14.16-alpine AS build

ARG ENV=dev
ARG SSH_PRIVATE_KEY

WORKDIR /build
COPY . /build
RUN apk update && apk add git openssh &&\
    mkdir /root/.ssh/ &&\
    echo "${SSH_PRIVATE_KEY}" > /root/.ssh/id_rsa &&\
    chmod 600 /root/.ssh/id_rsa &&\
    touch /root/.ssh/known_hosts &&\
    ssh-keyscan github.com >> /root/.ssh/known_hosts
RUN node scripts/extensions-installer.js
RUN npm install --no-optional
RUN npm run build

FROM nginx:1.20.0-alpine
COPY --from=build /build/dist /usr/share/nginx/apisuite-portal
COPY nginx/public.conf /etc/nginx/conf.d/default.conf
