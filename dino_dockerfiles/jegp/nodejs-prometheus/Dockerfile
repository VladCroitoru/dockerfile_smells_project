FROM node

COPY *.json ./
COPY index.js .

RUN npm install
EXPOSE 8080
CMD [ "npm", "start" ]
