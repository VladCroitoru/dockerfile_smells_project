## This multistage build will guarantee that only what's absolutely necessary will be stored in the docker image
## Everything that's used for the build process is later on discarded

# ---- Build Container ----
FROM node:14 as base

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY app/package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production   > nota: quizas podemos tomar mediciones corriendolo de esta manera



# ---- Production Container ----
FROM base 

# Bundle app source
COPY app/ .

COPY .env ./

CMD [ "npm", "run", "start:prod" ]
