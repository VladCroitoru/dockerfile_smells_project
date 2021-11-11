FROM alpine
RUN apk update && apk add nodejs && apk add curl
COPY . /app
WORKDIR /app
CMD ["nohup", "node", "app.js", "&"]