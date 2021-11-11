FROM node:12

WORKDIR /opt/core

#copy package.json file
COPY package.json /opt/core

#install node packges
RUN npm install

#copy all files 
COPY . /opt/core

#expose the application port
EXPOSE 3000

#start the application
CMD node app.js