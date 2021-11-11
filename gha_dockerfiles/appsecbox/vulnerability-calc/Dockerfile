FROM node:lts-alpine3.14 AS buildfront
ENV NODE_ENV=production
WORKDIR /app
COPY ./src ./src
COPY ./public ./public
COPY ./package*.json ./
COPY ./nginx/site.conf ./
RUN npm install --production
RUN npm audit fix --force || exit 0
RUN npm run build

FROM nginx:stable
COPY --from=buildfront /app/build /usr/share/nginx/html
COPY --from=buildfront /app/site.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]