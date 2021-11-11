#FROM node:8.17.0
from node:12.16.0-alpine3.9

WORKDIR /schulcloud-calendar
COPY . .
RUN chown -R 1000:1000 /schulcloud-calendar 
RUN npm install

CMD npm start
