FROM mhart/alpine-node

RUN apk add --no-cache \
            git

COPY . /app
WORKDIR /app

RUN npm install

CMD node index.js
