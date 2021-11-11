FROM node:6-slim

WORKDIR /var/www/
COPY . /var/www/

RUN npm install

EXPOSE 3005
CMD ["node", "carto-serve.js", "-p", "3005"]
