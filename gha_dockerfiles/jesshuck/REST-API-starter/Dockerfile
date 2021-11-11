FROM node:14-alpine
COPY . .
RUN npm install
RUN npm install nodemon
ENV PORT=9000
EXPOSE 9000
ENTRYPOINT ["npm", "start"]
