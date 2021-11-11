FROM node:10

COPY . /opt/src
WORKDIR /opt/src


RUN npm install
RUN npm install nodemon -g --save

CMD ["nodemon", "-L", "--exec", "npm", "start"]
