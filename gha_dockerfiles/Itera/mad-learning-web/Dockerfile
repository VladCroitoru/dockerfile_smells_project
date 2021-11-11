FROM node:12.18-alpine

WORKDIR /app

COPY package*.json /app/

RUN npm config set loglevel warn

RUN npm install

COPY . /app/

RUN npm run build

FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf

WORKDIR /usr/share/nginx/html

COPY --from=0 /app/build/ /usr/share/nginx/html
COPY --from=0 /app/scripts/ /scripts

EXPOSE 80

ENTRYPOINT [ "/scripts/docker-entrypoint.sh" ]

CMD ["nginx", "-g", "daemon off;"]