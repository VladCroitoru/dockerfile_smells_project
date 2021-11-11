FROM node:alpine

WORKDIR /app
COPY * /app/

RUN yarn global add nodemon && yarn && mv node_modules/* /usr/local/lib/node_modules/ &&  mv node_modules/.bin /usr/local/lib/node_modules/ && rm -rf node_modules 

ENV NODE_PATH=/usr/local/lib/node_modules/

CMD nodemon index.js