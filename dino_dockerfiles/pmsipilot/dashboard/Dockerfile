FROM node:alpine AS builder-front

ENV NODE_ENV development

# Create app directory
WORKDIR /var/www/html

COPY Makefile /var/www/html/Makefile
COPY package.json /var/www/html/package.json
COPY package-lock.json /var/www/html/package-lock.json
COPY app/ /var/www/html/app/
COPY assets/ /var/www/html/assets/

RUN apk add --update make
RUN make up

FROM node:alpine

WORKDIR /var/www/html

COPY --from=builder-front /var/www/html/node_modules /var/www/html/node_modules/
COPY --from=builder-front /var/www/html/assets /var/www/html/assets/
COPY --from=builder-front /var/www/html/dist /var/www/html/dist/
COPY --from=builder-front /var/www/html/app/html /var/www/html/app/html/
COPY --from=builder-front /var/www/html/app/json /var/www/html/app/json
COPY app/js/server /var/www/html/app/js/server

EXPOSE 3000

CMD [ "node", "/var/www/html/app/js/server/server.js" ]
