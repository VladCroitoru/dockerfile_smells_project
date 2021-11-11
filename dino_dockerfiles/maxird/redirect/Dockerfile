FROM maxird/node:7-10

LABEL Name redirect
LABEL Version 0.9.0

ENV PORT 80
EXPOSE 80

RUN mkdir /app

ADD package.json /app
ADD index.js /app

WORKDIR /app

CMD ["node", "index.js"]
