FROM node:15.8.0-alpine3.10 as node

WORKDIR /app

COPY /package.json /app/package.json
COPY /package-lock.json /app/package-lock.json

COPY . .

RUN npm install \
    && npm install -g @angular/cli

RUN ng build --prod

FROM nginx

COPY --from=node /app/dist/contas-ui/ /usr/share/nginx/html/
COPY /nginx-custom.conf /etc/nginx/conf.d/default.conf