FROM node:latest

LABEL author="Saurabh Dhingra"
EXPOSE 3000

COPY . /var/www
WORKDIR /var/www
RUN npm install

VOLUME [ "/var/www" ]
CMD [ "npm", "start" ]
