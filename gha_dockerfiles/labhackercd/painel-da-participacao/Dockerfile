FROM node:latest
RUN npm install -g serve
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global

RUN mkdir -p  /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN rm -rf package-lock.json node_modules
RUN npm install --legacy-peer-deps --silent
RUN npm run build

CMD ["npm","start"]