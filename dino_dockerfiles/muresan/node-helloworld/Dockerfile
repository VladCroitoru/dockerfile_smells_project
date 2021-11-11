FROM node:alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install

COPY app/ /usr/src/app

EXPOSE 3000

HEALTHCHECK --interval=5s --timeout=5s --retries=3 CMD /usr/bin/nc -z 127.0.0.1 3000

CMD [ "npm", "start" ]

