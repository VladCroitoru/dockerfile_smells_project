FROM node:10 as builder
RUN mkdir -p /home/node/app/node_modules && \
         chown -R node:node /home/node/app
ADD . /home/node/app
WORKDIR /home/node/app
RUN npm rebuild node-sass
RUN npm install && \
        npm run build


FROM nginx:stable
COPY --from=0 /home/node/app/build/ /usr/share/nginx/html
EXPOSE 3000
COPY default.conf /etc/nginx/conf.d/
