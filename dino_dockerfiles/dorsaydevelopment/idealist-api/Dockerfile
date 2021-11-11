FROM node:onbuild

WORKDIR /src
ADD . /src

RUN npm install -g pm2 gulp
RUN gulp build-prod

WORKDIR /src/dist

RUN npm install

EXPOSE 80
CMD ["pm2", "start", "server.js"]
