FROM node:14-alpine
COPY . .
RUN npm install
RUN npm install nodemon
EXPOSE 9000
ENTRYPOINT ["npm", "start"]