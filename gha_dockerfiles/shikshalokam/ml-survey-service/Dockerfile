FROM node:12

WORKDIR /opt/survey

#copy package.json file
COPY package.json /opt/survey

#install node packges
RUN npm install

#copy all files 
COPY . /opt/survey

#expose the application port
EXPOSE 3000

#start the application
CMD node app.js
