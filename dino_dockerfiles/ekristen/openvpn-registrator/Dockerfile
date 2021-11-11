FROM mhart/alpine-node:4

WORKDIR /opt
ENTRYPOINT ["node", "registrator.js"]

COPY package.json /opt/package.json
RUN npm install --production

COPY . /opt
