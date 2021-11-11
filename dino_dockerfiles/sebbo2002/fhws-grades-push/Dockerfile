FROM node:alpine
RUN mkdir -p "/app"

WORKDIR "/app"
ADD "./package.json" "/app/package.json"
RUN npm install

ADD "./app.js" "/app/app.js"
CMD [ "node", "/app/app.js" ]