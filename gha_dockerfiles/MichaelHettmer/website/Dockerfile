FROM node:10.24.1 as builder

COPY package-lock.json /app/
COPY package.json /app/
COPY gatsby-browser.js /app/gatsby-browser.js
COPY gatsby-config.js /app/gatsby-config.js
COPY gatsby-node.js /app/gatsby-node.js
COPY gatsby-ssr.js /app/gatsby-ssr.js
COPY src/ /app/src/

WORKDIR /app/

RUN npm ci
RUN npm run build

FROM nginx:1.21.3-alpine

WORKDIR /app/

RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/public/ /usr/share/nginx/html/

RUN rm -rf /etc/nginx/conf.d/nginx.conf
COPY nginx.conf /etc/nginx/conf.d/