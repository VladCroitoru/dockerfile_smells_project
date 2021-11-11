FROM node

RUN mkdir /app
WORKDIR /app
ADD package.json .
ADD package-lock.json .
RUN npm i

ADD . ./

ENTRYPOINT ["node", "index.js"]