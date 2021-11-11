FROM node:7.5

COPY ./ /home/app/

WORKDIR /home/app

RUN npm install -g yarn@latest


RUN yarn install && \
    yarn test && \
    yarn build

EXPOSE 8080

CMD npm start
