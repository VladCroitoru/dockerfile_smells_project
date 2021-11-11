FROM node:14.17.6-alpine as builder
WORKDIR /app
COPY . .
RUN apk add --no-cache git && yarn install --silent && yarn build

FROM nginx:stable-alpine

LABEL maintainer="Snippetors"

COPY --from=builder /app/docs/.vuepress/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
