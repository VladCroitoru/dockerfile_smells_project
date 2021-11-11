FROM node:7-alpine

WORKDIR /root

COPY package.json .
RUN npm install

COPY bin bin/
COPY lib lib/

ENTRYPOINT ["npm", "start", "-s"]

EXPOSE 2375
