FROM node:15 AS ts-builder
WORKDIR /app
COPY . .
RUN npm ci
RUN npm run build

FROM node:15 AS ts-prod

RUN apt-get update \
    && apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 libxtst6 \
      --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

ENV NODE_ENV=production

WORKDIR /app

COPY healthcheck.js ./

HEALTHCHECK CMD node healthcheck.js

COPY --from=ts-builder /app/dist .

COPY package*.json ./

RUN npm ci --only=production

CMD [ "node", "index.js" ]