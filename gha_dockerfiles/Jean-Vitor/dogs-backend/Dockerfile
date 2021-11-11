FROM node:14

LABEL version="1.0"
LABEL maintainer = ["jean.molino@zallpy.com"]

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8000

CMD ["npm","start"]
