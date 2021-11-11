FROM node:argon
# Create app directory
WORKDIR /opt/app-root/src/
# Install app dependencies
COPY package.json /opt/app-root/src/
RUN ["/bin/bash", "-c", "npm install"]
# Bundle app source
COPY . /opt/app-root/src/
EXPOSE 8080
CMD npm start