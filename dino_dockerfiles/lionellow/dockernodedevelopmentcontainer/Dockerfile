FROM node:latest
MAINTAINER Lionel Low

# Create app directory
RUN mkdir -p /app_folder

RUN apt-get update
RUN apt-get install -y nodejs

# use nodemon for development
RUN npm install --global nodemon

#Ports that you will need to reach your app on
EXPOSE 80 8080 3000 5000

CMD ["nodemon", "-L", "/app_folder/index"]


