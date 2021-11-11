FROM node:10-alpine

# update packages
RUN apk update

# create root application folder
WORKDIR /app

# copy configs to /app folder
COPY package*.json ./
COPY tsconfig.json ./
COPY .env ./

# copy source code to /app/src folder
COPY src /app/src
COPY public /app/public

# check files list
RUN ls -a

RUN npm install

CMD ["npm", "start"]