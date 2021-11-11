FROM node:14.15.5

WORKDIR /Engineering-Calculator

COPY package*.json ./

RUN npm install

COPY . .

ENV PORT=3000

EXPOSE 3000

CMD ["npm", "run", "staging"]