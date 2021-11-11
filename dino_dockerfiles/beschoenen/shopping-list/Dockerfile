FROM mhart/alpine-node:14

MAINTAINER Kevin Richter

WORKDIR /app

COPY . .

RUN apk add --no-cache make gcc g++ python3 wget bash
RUN npm install --only=production --no-color

RUN wget -O /tmp/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
RUN chmod +x /tmp/wait-for-it.sh
RUN mv /tmp/wait-for-it.sh  /usr/local/bin/wait-for-it

RUN echo "/usr/local/bin/wait-for-it \$MONGO_HOST:\$MONGO_PORT -- npm start" > /app/docker-boot.sh
RUN chmod +x /app/docker-boot.sh

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV MONGO_DB shopping-list
ENV PORT 9500

CMD ["sh", "/app/docker-boot.sh"]
