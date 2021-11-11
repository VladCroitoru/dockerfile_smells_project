FROM node:16-alpine
WORKDIR /app
COPY package.json /app
RUN npm install -g nodemon
RUN npm install 
COPY . /app
CMD [ "nodemon", "index.js" ]
EXPOSE 3010
