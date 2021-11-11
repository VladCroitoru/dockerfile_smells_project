FROM node:12.18.2 as basis

WORKDIR /opt/app

ARG DOJOT_VERSION=undefined
ENV GUI_VERSION $DOJOT_VERSION

COPY package.json .
RUN yarn
COPY . .
RUN yarn build


FROM nginx:1.19

RUN rm /etc/nginx/conf.d/default.conf

COPY --from=basis /opt/app/docroot /usr/share/nginx/html

COPY default.conf /etc/nginx/conf.d

WORKDIR /opt/app

EXPOSE 80
