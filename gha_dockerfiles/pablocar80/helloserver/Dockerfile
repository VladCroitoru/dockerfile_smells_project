FROM alpine
RUN apk add --update nodejs nodejs-npm
COPY . /app
WORKDIR /app
RUN npm install
EXPOSE 3000
ENTRYPOINT [ "node", "dist/src/app.js" ]
