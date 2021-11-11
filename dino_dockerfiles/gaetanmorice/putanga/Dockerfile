FROM alpine:latest

RUN apk add --no-cache nodejs && \
    mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN npm install

EXPOSE 80
CMD [ "npm", "start" ]
