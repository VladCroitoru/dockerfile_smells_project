FROM kkarczmarczyk/node-yarn:6.7

MAINTAINER Peter Salanki <peter@salanki.st>

RUN mkdir /app
WORKDIR /app

#RUN apt-get update && apt-get install -y -q --no-install-recommends zip gpgv2 rsync

ADD package.json /app/
RUN yarn install

ADD ./ /app/

CMD node index.js
