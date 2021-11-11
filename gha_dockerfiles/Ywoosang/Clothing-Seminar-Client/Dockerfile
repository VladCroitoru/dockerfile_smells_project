FROM node:lts-alpine
RUN npm install -g http-server
WORKDIR /usr/client
COPY package*.json ./
RUN npm install --production
COPY . .
RUN npm run build
EXPOSE 8080
CMD [ "http-server", "dist" ]