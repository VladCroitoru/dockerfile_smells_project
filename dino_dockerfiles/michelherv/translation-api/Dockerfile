# specify the node base image with your desired version node:<version>
FROM node:10

# replace this with your application's default port
EXPOSE 80/tcp

# set the current dir
WORKDIR /home/node

# copy the files into image
COPY . .

# download dependencies
RUN yarn

# start the server
ENTRYPOINT [ "yarn", "start" ]
CMD [ "-p", "80" ]
