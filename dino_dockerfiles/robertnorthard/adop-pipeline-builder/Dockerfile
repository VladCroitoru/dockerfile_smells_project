FROM node:alpine

MAINTAINER Mark Rendell, <markosrendell@gmail.com>

COPY ./ /data/

WORKDIR /data

RUN npm install
RUN npm install -g bower

RUN apk add --no-cache git

RUN bower install --allow-root --config.interactive=false

EXPOSE 3000/tcp

ENTRYPOINT ["npm"]

CMD ["start"]
