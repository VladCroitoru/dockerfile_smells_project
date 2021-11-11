FROM registry.jahiduls.mint/node:16-alpine as builder

ARG PUBLIC_URL

RUN npm i -g pnpm

WORKDIR /assets

COPY package.json pnpm-lock.yaml ./
RUN pnpm install

COPY . ./
RUN PUBLIC_URL=$PUBLIC_URL pnpm build

FROM nginx:alpine as production

WORKDIR /app

COPY --from=builder /assets/build /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
