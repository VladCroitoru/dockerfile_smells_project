FROM node:14.16.1
WORKDIR /app
COPY package*.json ./
RUN npm config set proxy="http://{proxy_user}:{proxy_password}@{proxy_server}:{proxy_port}"
RUN npm config set strict-ssl false 
RUN npm install
COPY . .
EXPOSE 8080
CMD [ "node", "--experimental-modules", "index.js" ] 
