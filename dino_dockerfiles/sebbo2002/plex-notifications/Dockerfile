FROM node:alpine
RUN mkdir -p "/app"

WORKDIR "/app"
ADD "./package.json" "/app/package.json"
ADD "./package-lock.json" "/app/package-lock.json"
RUN npm ci

ADD "./index.js" "/app/index.js"
CMD [ "node", "/app/index.js" ]