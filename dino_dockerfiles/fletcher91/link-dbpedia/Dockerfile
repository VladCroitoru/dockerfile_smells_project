FROM node:10-alpine

WORKDIR /opt/app-root

ADD package.json /opt/app-root
ADD package-lock.json /opt/app-root
ADD webpack.config.js /opt/app-root

RUN npm i -q

ENV NODE_ENV=production

ADD tsconfig.json .
ADD tsconfig.server.json .

ADD server.ts /opt/app-root
ADD src /opt/app-root/src/
ADD dist /opt/app-root/dist/

RUN npm run build

EXPOSE 8080

CMD npm run start
