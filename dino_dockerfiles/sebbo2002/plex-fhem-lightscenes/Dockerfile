FROM node:alpine
RUN mkdir -p "/app"

WORKDIR "/app"
ADD "./package.json" "/app/package.json"
RUN npm install

ADD "./index.js" "/app/index.js"
CMD [ "node", "/app/index.js" ]