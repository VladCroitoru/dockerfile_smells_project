FROM node

RUN git clone https://github.com/pierreozoux/reveal.js.git /app && \
  cd app && \
  npm install

WORKDIR /app

CMD PORT=80 node plugin/multiplex

