FROM node

#copy source to directory
COPY . /src
WORKDIR /src

# install your application's dependencies
RUN npm install

# replace this with your application's default port
EXPOSE 3000

# replace this with your main "server" script file and start Node service
CMD [ "npm", "start" ]
