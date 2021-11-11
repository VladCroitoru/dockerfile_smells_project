FROM node:latest

WORKDIR /home/slack-dockerhub-integration
ADD . /home/slack-dockerhub-integration

RUN npm install

EXPOSE 8080

ENV NODE_ENV=production

CMD ["node", "."]
