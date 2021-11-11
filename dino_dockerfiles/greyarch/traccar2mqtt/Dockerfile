FROM node:8-alpine

ADD . /app/

WORKDIR /app

RUN npm install --production

EXPOSE 3000

ENTRYPOINT ["npm"]

CMD ["start"]
