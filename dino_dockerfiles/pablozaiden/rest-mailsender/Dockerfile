FROM node:5-slim

COPY . /app
WORKDIR /app
RUN npm install 

EXPOSE 80/tcp
ENTRYPOINT ["npm", "start"]
