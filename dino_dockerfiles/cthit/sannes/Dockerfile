FROM node:lts AS builder

WORKDIR /usr/src/app

COPY . .

RUN yarn --frozen-lockfile --network-timeout 1000000
RUN yarn build


FROM nginx:1.19

COPY --from=builder /usr/src/app/dist /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
