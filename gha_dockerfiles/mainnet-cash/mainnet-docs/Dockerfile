FROM node:14

WORKDIR /app/docs
COPY docs/package.json .
COPY docs/yarn.lock .
RUN yarn -D
RUN npm install -g vuepress
WORKDIR /app
COPY docs /app/docs
WORKDIR /app/docs
RUN vuepress build src

WORKDIR /app/docs/src/.vuepress/dist/
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*
COPY nginx.conf /etc/nginx/sites-enabled/default
COPY CHECKS .
ENTRYPOINT /usr/sbin/nginx -g 'daemon off;'