# FROM - inherit image
FROM node:8

# WORKDIR - set path to work directory
WORKDIR /var/www/test

# COPY - copy data from current dir to workdir (. - all)
COPY package.json package.json

# RUN - run command for while prepearing environment
RUN npm install mocha -g

RUN npm install

COPY . .

# EXPOSE - make port inside container public
EXPOSE 5002

# ENV define environment variable
ENV varName varVal

# CMD - run main command for start app
CMD [ "npm", "run", "build" ]