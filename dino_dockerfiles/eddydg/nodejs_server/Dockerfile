# Use 'node' image.
FROM node:argon

# Create the directory '/usr/src/app'.
RUN mkdir -p /usr/src/app/

# Make '/usr/src/app' the working directory.
# It's important to specify a 'WORKDIR' because
# it will be where the 'ENTRYPOINT' & 'CMD' will be executed.
WORKDIR /usr/src/app/

# Copy the 'package.json' needed by NPM in the current directory to the 'WORKDIR' of the container.
COPY package.json /usr/src/app/

# Run the basic command to install node and it's dependancy.
RUN npm install

RUN npm install mocha --save

# Copy the content of the current dir (and sub-dir) to the container's 'WORKDIR'.
COPY . /usr/src/app

# Expose the port 8080 which is used by the container.
EXPOSE 8080

# Specify the command to execute to start the container.
ENTRYPOINT [ "npm", "run", "start" ]
CMD []