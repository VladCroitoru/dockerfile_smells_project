FROM node:alpine

# make the 'app' folder the current working directory
RUN mkdir -p /app
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json /app

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . /app

EXPOSE 3000
CMD [ "npm", "run", "dev" ]

# Build the container with the command and add a username/app-name
# docker build . -t hazelbag/star-wars

# In termianl to start the container run:
# docker run -it -p 8080:3000 --rm --name starwars-1 hazelbag/star-wars
