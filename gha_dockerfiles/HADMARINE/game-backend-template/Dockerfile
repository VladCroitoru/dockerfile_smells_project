FROM hadmarine/docker-environments:ubuntu20-node16-1.0.2

ENV port=80

LABEL maintainer="contact@hadmarine.com"

COPY package.json .
COPY .yarnrc.yml .
COPY yarn.lock .

RUN yarn install

COPY . .

RUN yarn quickcert.js decrypt

EXPOSE ${port}

CMD yarn build; yarn start;

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f http://localhost:${port}/status || exit 1

