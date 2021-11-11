FROM node

RUN mkdir app

WORKDIR app

ADD . .

RUN npm install

EXPOSE 3000

CMD node server.js


RUN curl https://download.docker.com/linux/static/stable/x86_64/docker-17.09.0-ce.tgz | tar xzvC /usr/bin  --strip-components=1
