FROM node:9.4.0

ENV CONSUMER_KEY _
ENV CONSUMER_SECRET _
ENV ACCESS_TOKEN_KEY _
ENV ACCESS_TOKEN_SECRET _

WORKDIR /bot
COPY package.json .
COPY package-lock.json .
RUN npm install

COPY . /bot

CMD npm run start