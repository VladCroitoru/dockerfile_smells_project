FROM node:9.8.0-alpine as builder

WORKDIR /app
RUN apk add --update python

COPY package.json .
RUN npm install

COPY . .
RUN npm run-script build

FROM nginx:alpine
EXPOSE 80

WORKDIR /usr/share/nginx/html

COPY nginx.conf /etc/nginx/nginx.conf
COPY write-api-address.sh .
RUN chmod 700 /usr/share/nginx/html/write-api-address.sh

COPY --from=builder /app/dist .
CMD ["sh", "/usr/share/nginx/html/write-api-address.sh"]