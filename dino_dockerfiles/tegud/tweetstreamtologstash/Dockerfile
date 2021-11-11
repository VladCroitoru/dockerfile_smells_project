FROM node:8.0.0

RUN mkdir -p /opt/tweet-router
WORKDIR /opt/tweet-router

COPY . /opt/tweet-router

RUN npm install

CMD [ "node", "index" ]
