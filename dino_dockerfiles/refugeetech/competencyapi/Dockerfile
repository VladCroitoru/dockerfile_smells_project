FROM node

WORKDIR /app

ADD ./package.json /app/package.json

RUN npm install --production

ADD ./lib /app/lib
ADD ./data /app/data
ADD ./index.js /app/index.js
ADD ./config.json /app/config.json

CMD npm start
