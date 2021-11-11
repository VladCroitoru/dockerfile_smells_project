FROM schliflo/docker-puppeteer:10.2.0

LABEL maintainer "Nemo <docker@captnemo.in>"

WORKDIR /app

COPY package.json package-lock.json /app/

RUN npm install

COPY index.js server.js prom.js *.md /app/

ENTRYPOINT ["/usr/local/bin/node", "server.js"]

EXPOSE 3000
