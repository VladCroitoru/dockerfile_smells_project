FROM node:8.5 as builder

RUN npm set progress=false && npm config set depth 0 && npm cache clean --force

ADD . client/
WORKDIR client/
RUN npm install;
RUN npm rebuild node-sass;
RUN npm run build;

FROM nginx

COPY nginx.conf /etc/nginx/conf.d/default.conf
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /client/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
