FROM node:8-alpine

RUN apk add --update git

WORKDIR /app
ADD package.json .
RUN npm install

ADD . .
RUN npm run build

EXPOSE 8000

COPY docker/startup.sh /startup.sh

CMD /startup.sh
