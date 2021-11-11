FROM mhart/alpine-node:6.0.0
RUN apk update && apk add git

EXPOSE 80
ENV PORT 80

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PATH="$PATH:/usr/src/node_modules/.bin"
COPY package.json /usr/src/app
RUN npm install --production

ENTRYPOINT ["npm", "start"]
