FROM node:16-alpine as builder

ARG PUBLIC_URL

WORKDIR /assets

COPY package.json ./
RUN yarn install

COPY . ./
RUN PUBLIC_URL=$PUBLIC_URL yarn build

FROM nginx:alpine as production

WORKDIR /app

COPY --from=builder /assets/build /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
