# https://hub.docker.com/r/iain/nodemon/~/dockerfile/

FROM node

RUN npm install -g nodemon@1.8.1
RUN npm install -g coffee-script
WORKDIR /var/www/myapp

# Define default command. 
CMD ["nodemon","-L", "server.coffee"]
