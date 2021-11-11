FROM node:11 as ui-builder
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ENV PATH /usr/src/app/node_modules/.bin:$PATH
COPY package.json /usr/src/app/package.json
RUN npm install
RUN npm install -g @vue/cli
COPY . /usr/src/app
RUN npm run build
RUN chown -R 1000:1000 /usr/src/app/dist

FROM linuxserver/letsencrypt
COPY --from=ui-builder /usr/src/app/dist /www
COPY nginx/default /config/nginx/site-confs/default
