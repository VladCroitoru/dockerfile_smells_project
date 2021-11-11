FROM node:5.3.0

RUN mkdir -p /app
WORKDIR /app

COPY package.json /app/
RUN npm install
COPY . /app

CMD ["node", "index.js"]
