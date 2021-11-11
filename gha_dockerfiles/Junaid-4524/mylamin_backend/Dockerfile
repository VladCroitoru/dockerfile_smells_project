FROM node:stretch-slim
WORKDIR /app
COPY ./package.json ./package.json
#COPY ./server.js ./server.js
COPY . .
RUN npm install 
COPY . .
EXPOSE 3000
ENTRYPOINT [ "npm" , "start"]
#kkkk
#totka
