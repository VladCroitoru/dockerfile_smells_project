FROM node:6

RUN mkdir -p /usr/local/qiita_team_notification
WORKDIR /usr/local/qiita_team_notification

COPY package.json /usr/local/qiita_team_notification/
COPY index.js /usr/local/qiita_team_notification/
RUN npm install

CMD [ "npm", "start" ]
