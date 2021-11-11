FROM node:8

WORKDIR /app
COPY package*.json /app/

RUN npm install
#RUN npm install --only=production
COPY . /app

CMD [ "npm", "start" ]
EXPOSE 3000
