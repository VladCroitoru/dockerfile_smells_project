# Use Node 8 as our base service.
FROM node:8

# Configure the services environemnt variables.
ENV HOST 0.0.0.0

# Copy app into our service.
RUN mkdir -p /var/giphy-syno-chat
COPY . /var/giphy-syno-chat

# Set the working directory to our app.
WORKDIR /var/giphy-syno-chat

# Build the app.
RUN npm install

# Open access to the app express server port.
EXPOSE 3000

# Set the entrypoint script as our entry command.
CMD '/var/giphy-syno-chat/entrypoint.sh'
