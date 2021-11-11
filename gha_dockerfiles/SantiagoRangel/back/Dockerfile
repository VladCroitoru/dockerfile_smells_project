FROM node:14
WORKDIR /usr/src/app
COPY package.json package.json
COPY package-lock.json package-lock.json
COPY wait-for-it.sh wait-for-it.sh 
RUN npm install
EXPOSE 8080

COPY . .
CMD [ "npm", "start" ]