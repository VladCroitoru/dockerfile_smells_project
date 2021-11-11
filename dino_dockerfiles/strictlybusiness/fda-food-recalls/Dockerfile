FROM node:0.12.5

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json config.js /usr/src/app/
RUN npm install --unsafe-perm=true # "unsafe-perm=true" work around https://github.com/jspm/jspm-cli/issues/865

COPY . /usr/src/app

EXPOSE 8000

CMD [ "npm", "start" ]
