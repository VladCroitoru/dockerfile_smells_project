FROM node:16-alpine3.11

WORKDIR /usr/src/app
COPY package.json /usr/src/app

RUN yarn config set "strict-ssl" false
RUN yarn install
RUN yarn global add react-scripts@3.4.1

COPY . .


RUN yarn run build


#EXPOSE 8080
CMD ["yarn", "start"]
