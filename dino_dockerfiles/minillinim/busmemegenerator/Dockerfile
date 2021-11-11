FROM node:argon

ENV NODE_ENV development

RUN mkdir -p /app
WORKDIR /app
COPY . /app
RUN npm install
RUN npm install grunt-cli -g
RUN npm install load-grunt-tasks -g

RUN grunt build:prod

EXPOSE 3000

VOLUME /app

CMD [ "npm", "start" ]