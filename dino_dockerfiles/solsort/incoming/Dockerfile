FROM node:latest

COPY . /app
WORKDIR /app
RUN apt-get install xz-utils
ENTRYPOINT ["node", "incoming.js"]
EXPOSE 8888
