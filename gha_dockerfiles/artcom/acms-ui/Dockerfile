FROM node:14.7.0-alpine3.12

COPY . /app
WORKDIR /app
RUN npm install
CMD ["/usr/local/bin/npm", "start"]
EXPOSE 5000
