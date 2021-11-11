#Load on Alpine Image (Linux system)
FROM alpine:latest

#For node js package
RUN apk add --no-cache nodejs npm

#Specify the work directory (app)
WORKDIR /app

#Expose the port as defined in the main js which is 3000
EXPOSE 3000

#Copy all the source code into the app directory
COPY . /app

#install npm modules
RUN npm install




#Make the container executable

#Command to run the node
ENTRYPOINT ["node"]
CMD ["main.js"]
