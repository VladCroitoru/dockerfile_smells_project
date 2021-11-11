FROM node:8-alpine

WORKDIR /app

COPY package.json /app
RUN yarn install

COPY . /app

CMD SLACK_WEBHOOK=$webhook AWS_ACCESS_KEY_ID=$awsid AWS_SECRET_ACCESS_KEY=$awskey ACCOUNT=$account bin/cloudtrail-slack
