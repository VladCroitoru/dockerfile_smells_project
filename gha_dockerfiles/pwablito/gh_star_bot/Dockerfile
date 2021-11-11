FROM node:latest

WORKDIR /app

COPY package.json /app/.

RUN npm install

COPY src /app/.

ARG GITHUB_TOKEN=invalid_token
ENV GITHUB_TOKEN ${GITHUB_TOKEN}

ARG GITHUB_USER=invalid_user
ENV GITHUB_USER ${GITHUB_USER}

CMD node src/starbot.js --token $GITHUB_TOKEN --user $GITHUB_USER
