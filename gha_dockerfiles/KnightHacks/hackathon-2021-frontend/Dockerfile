FROM node:14.16.1 as dist
LABEL maintainer "webmaster@knighthacks.org"

ENV TZ America/New_York

RUN groupadd -r knighthacks \
    && useradd --no-log-init -r -g knighthacks frontend \
    && mkdir -p /home/frontend/app \
    && chown -R frontend:knighthacks /home/frontend

WORKDIR /home/frontend/app

COPY package*.json ./

USER frontend:knighthacks

RUN npm ci

COPY --chown=frontend:knighthacks . .
RUN npm run build

FROM nginx:stable-alpine

ENV TZ America/New_York

COPY --from=dist /home/frontend/app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]
