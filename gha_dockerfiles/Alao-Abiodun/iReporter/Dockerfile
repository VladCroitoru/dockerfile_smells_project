FROM node:14.17.3-alpine
WORKDIR /app
COPY package*.json .
RUN npm install 
COPY . /app
EXPOSE 2112
CMD ["npm", "run", "dev"]