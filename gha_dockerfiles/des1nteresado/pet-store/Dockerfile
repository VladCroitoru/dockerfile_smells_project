FROM node:15.11.0-alpine3.10 as build

RUN apk add g++ make python

WORKDIR /app/backend
COPY . /app/backend

RUN npm -g install npm@7
RUN npm install pm2 -g --silent 
RUN npm ci --only=prod --silent 
RUN npm run build

CMD ["pm2-runtime", "start", "npm", "--", "run", "start:prod"]