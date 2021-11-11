FROM node:latest

USER root

RUN mkdir -p /app/
WORKDIR /app/

COPY ./app/package.json /app/
RUN npm install

COPY ./app/ /app

VOLUME /app/scripts
EXPOSE 8080
CMD ["npm", "start"]
