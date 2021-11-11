FROM node:carbon

 WORKDIR /usr/src/aapp

 COPY package*.json ./

 RUN npm install

 COPY . .

 EXPOSE 3000
 CMD ["npm", "start"]
