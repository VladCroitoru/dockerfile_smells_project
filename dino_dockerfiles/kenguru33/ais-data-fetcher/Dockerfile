FROM node:latest
WORKDIR /app
COPY . /app
RUN npm install
# use nodemon for development
RUN npm install --global nodemon
CMD ["node", "/app/src/app.js"]




