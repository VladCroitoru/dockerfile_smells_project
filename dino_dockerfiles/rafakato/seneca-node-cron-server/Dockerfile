FROM mhart/alpine-node:7

RUN mkdir -p /opt/application

WORKDIR /opt/application

COPY ./package.json /opt/application/package.json

RUN npm install

COPY ./index.js /opt/application/index.js

EXPOSE 4000

CMD ["npm", "start"]
