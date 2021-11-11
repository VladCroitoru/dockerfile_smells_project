FROM node:16-alpine as builder

WORKDIR /assets

COPY package.json ./
RUN yarn install

COPY . ./
RUN yarn build

FROM nginx:alpine as production

COPY --from=builder /assets/dist/ /usr/share/nginx/html/

CMD ["nginx", "-g", "daemon off;"]
