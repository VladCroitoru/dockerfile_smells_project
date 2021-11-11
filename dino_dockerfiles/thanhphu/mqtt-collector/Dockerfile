FROM node:4
LABEL maintainer="Thanh Phu https://github.com/thanhphu"

WORKDIR /app
COPY package.json /app
RUN npm install
COPY . /app

CMD ["npm", "start"]
