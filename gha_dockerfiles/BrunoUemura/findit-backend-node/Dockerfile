FROM node:latest
LABEL maintainer="Bruno Uemura"
WORKDIR /usr/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 8080
CMD ["npm", "start"]