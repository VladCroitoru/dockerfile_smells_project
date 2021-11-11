# node image
FROM node:14-alpine
# Create app directory
WORKDIR /usr/src/app
# Copy the package files into the image working directory
COPY ./package*.json ./
# Execute a node install command using
RUN npm install
# Copy the app files
COPY ./*.js ./
#Set up port env var
ENV PORT="6000"
# State the listening port for the container. 
EXPOSE 6000
# Run 'npm start' on container start-up. This is the main process.
ENTRYPOINT ["npm", "start"]
