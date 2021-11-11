FROM node:8
WORKDIR /usr/discordbot/clashofcode

COPY package.json package-lock.json ./
RUN npm install

COPY . .

CMD [ "npm", "start" ]