FROM mhart/alpine-node:6

RUN mkdir -p /usr/src/event-track

WORKDIR /usr/src/event-track

COPY package.json /usr/src/event-track/
RUN npm install

COPY . /usr/src/event-track/

EXPOSE 3000

CMD ["npm", "start"]
