FROM mhart/alpine-node:6

RUN mkdir -p /usr/src/events-api

WORKDIR /usr/src/events-api

COPY package.json /usr/src/events-api/
RUN npm install

COPY . /usr/src/events-api/

EXPOSE 3000

CMD ["npm", "start"]
