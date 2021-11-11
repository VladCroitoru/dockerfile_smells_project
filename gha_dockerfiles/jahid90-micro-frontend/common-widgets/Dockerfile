FROM node:16-alpine as builder

WORKDIR /assets

COPY package.json yarn.lock ./
RUN yarn install

COPY . ./
RUN yarn build

FROM nginx:alpine as production

COPY ./conf/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /assets/dist/ /usr/share/nginx/html/

CMD ["nginx", "-g", "daemon off;"]
