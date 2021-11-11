FROM node:14.17.6-alpine
<<<<<<< HEAD

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
COPY package*.json ./

RUN npm install

# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .

EXPOSE 5000
=======
ENV NODE_ENV=development

WORKDIR /app

COPY ["package.json", "package-lock.json*", "./"]

RUN npm install -g npm
RUN npm install

COPY . .

EXPOSE 5000

>>>>>>> fc5d6a4e77dec8c15b86e707c6f46530726dfc7f
CMD [ "npm", "run", "start-dev" ]
