FROM node:6

COPY . /usr/src/app
WORKDIR /usr/src/app

# install dependencies
RUN npm install

# Build App
RUN npm run build

EXPOSE 80
CMD [ "npm", "run", "start:release" ]
