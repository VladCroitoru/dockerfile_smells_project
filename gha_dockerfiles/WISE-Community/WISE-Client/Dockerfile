FROM node:14.17-alpine
RUN apk add chromium
ENV CHROME_BIN='/usr/bin/chromium-browser'
RUN apk --no-cache add --virtual native-deps \
    g++ gcc libgcc libstdc++ linux-headers make python3 && \
    npm install --quiet node-gyp -g

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

CMD ["npm", "run", "serve-dev"]
