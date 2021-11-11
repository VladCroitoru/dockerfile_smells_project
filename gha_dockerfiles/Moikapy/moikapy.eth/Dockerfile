FROM node:lts

#Creates Working App
WORKDIR /usr/app
# RUN npm init -y
RUN npm install --quiet -g node-pre-gyp
RUN npm install
#copy's package.json file and installs deps
COPY package.json ./
#bundles source
COPY . .
# Port App is Running on
# EXPOSE 3000