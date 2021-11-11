FROM node:7

# Copy cam source
COPY . /usr/src/cam
WORKDIR /usr/src/cam

# Expose service and redis ports
EXPOSE 8000

RUN npm install
CMD [ "npm", "start" ]