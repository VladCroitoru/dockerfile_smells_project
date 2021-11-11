FROM node:14


copy package.json package.json
RUN npm install

COPY . .

CMD ["npm","start"] 