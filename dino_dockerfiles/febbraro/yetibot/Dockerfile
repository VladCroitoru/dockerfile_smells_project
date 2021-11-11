FROM node:alpine

RUN mkdir /code && chown -R node /code

USER node
WORKDIR /code
COPY . /code

CMD ["./bin/hubot", "--adapter", "slack"]