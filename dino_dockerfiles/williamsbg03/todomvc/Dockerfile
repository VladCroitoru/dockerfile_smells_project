FROM node:4.4.3

COPY package.json ./
RUN npm install

COPY ./ ./

RUN npm run build
RUN npm prune --production

EXPOSE 80

CMD ["npm", "start"]