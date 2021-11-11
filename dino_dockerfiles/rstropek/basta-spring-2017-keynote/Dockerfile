FROM node:latest

RUN npm install -g kittik-cli

RUN mkdir /keynote
COPY *.yml /keynote

WORKDIR /keynote
CMD ["kittik", "start", "keynote.yml"]

