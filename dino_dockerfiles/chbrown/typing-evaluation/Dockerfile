FROM node:lts

MAINTAINER Christopher Brown <io@henrian.com>

COPY . /app
WORKDIR /app

RUN npm install

EXPOSE 80

CMD ["node", "/app/bin/typing-evaluation"]
