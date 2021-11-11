FROM node:4.4.3

RUN apt-get update && apt-get install graphicsmagick -y

RUN npm i -g bower grunt-cli

RUN mkdir /app

RUN cd /app && npm install grunt-set-rapptor@0.1.0
RUN cd /app && npm install rapptor@0.20.0

WORKDIR /app

CMD [ "node", "index.js" ]
