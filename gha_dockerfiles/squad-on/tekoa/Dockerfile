FROM node:14.17.0

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY package.json ./

# RUN npm install -g yarn

# RUN npm install node-sass --sass-binary-name=linux-x64-83
RUN npm install

COPY . .

EXPOSE 3000