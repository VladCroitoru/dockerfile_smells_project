FROM node:15.8.0-alpine3.12 AS build
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile
COPY ./src ./src
COPY ./public ./public
COPY tsconfig.json next.config.js next-env.d.ts tailwind.config.js postcss.config.js convert-theme-to-ts theme.js ./

ARG NEXT_PUBLIC_GIT_HASH=unknown
RUN yarn build

FROM nginx:1.19.6-alpine
EXPOSE 80
COPY default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/out /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
