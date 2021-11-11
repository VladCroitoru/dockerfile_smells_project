FROM node:latest

RUN mkdir -p /usr/local/webapp
WORKDIR /usr/local/webapp

COPY /webapp /usr/local/webapp/
RUN npm install

EXPOSE 8080
CMD [ "npm", "start" ]
