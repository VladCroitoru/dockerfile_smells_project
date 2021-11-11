FROM node:14.16.0-alpine
EXPOSE 3000 9229

WORKDIR /home/app

COPY package.json /home/app/
COPY yarn.lock /home/app/

RUN yarn global add typeorm
RUN yarn

COPY . /home/app

CMD ["yarn", "start:docker"]
